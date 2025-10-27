#!/usr/bin/env python3
"""
Sistema de Validación y Progreso del Laboratorio AWS AI/ML
Este módulo proporciona funcionalidades para validar el progreso y logros del laboratorio.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

class LaboratoryValidator:
    """Sistema de validación y seguimiento de progreso del laboratorio"""
    
    def __init__(self, lab_path: str = "."):
        self.lab_path = lab_path
        self.progress_file = os.path.join(lab_path, "progress.json")
        self.modules = {
            "01-rekognition": {
                "name": "Análisis de Imágenes con Amazon Rekognition",
                "checkpoints": ["client_configured", "image_analyzed", "results_visualized"],
                "required_variables": ["rekognition", "image_analysis_result"],
                "points": 100
            },
            "02-comprehend": {
                "name": "Procesamiento de Texto con Amazon Comprehend",
                "checkpoints": ["client_configured", "text_analyzed", "entities_extracted"],
                "required_variables": ["comprehend", "text_analysis_result"],
                "points": 100
            },
            "03-textract": {
                "name": "Extracción de Texto con Amazon Textract",
                "checkpoints": ["client_configured", "document_processed", "text_extracted"],
                "required_variables": ["textract", "document_analysis_result"],
                "points": 100
            },
            "04-polly": {
                "name": "Síntesis de Voz con Amazon Polly",
                "checkpoints": ["client_configured", "audio_generated", "audio_played"],
                "required_variables": ["polly", "audio_result"],
                "points": 100
            },
            "05-bedrock": {
                "name": "IA Generativa con Amazon Bedrock",
                "checkpoints": ["client_configured", "content_generated", "parameters_tested"],
                "required_variables": ["bedrock_runtime", "seismic_report"],
                "points": 150
            },
            "06-q-developer": {
                "name": "Asistencia de Código con Amazon Q Developer",
                "checkpoints": ["client_configured", "code_generated", "code_executed"],
                "required_variables": ["q_developer", "generated_code_result"],
                "points": 150
            }
        }
        self.badges = {
            "first_steps": {
                "name": "🚀 Primeros Pasos",
                "description": "Completar el primer módulo",
                "condition": lambda progress: sum(1 for m in progress.values() if m.get('completed', False)) >= 1
            },
            "ai_explorer": {
                "name": "🔍 Explorador de IA",
                "description": "Completar 3 módulos",
                "condition": lambda progress: sum(1 for m in progress.values() if m.get('completed', False)) >= 3
            },
            "ml_master": {
                "name": "🎓 Maestro ML",
                "description": "Completar todos los módulos",
                "condition": lambda progress: sum(1 for m in progress.values() if m.get('completed', False)) == 6
            },
            "perfectionist": {
                "name": "⭐ Perfeccionista",
                "description": "Obtener puntuación perfecta en todos los módulos",
                "condition": lambda progress: all(
                    m.get('score', 0) == self.modules[mid]['points'] 
                    for mid, m in progress.items() 
                    if mid in self.modules
                )
            },
            "speed_runner": {
                "name": "⚡ Velocista",
                "description": "Completar el laboratorio en menos de 90 minutos",
                "condition": lambda progress: self._check_completion_time(progress, 90)
            }
        }
        self.load_progress()
    
    def load_progress(self) -> Dict[str, Any]:
        """Carga el progreso desde archivo"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    self.progress = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.progress = self._create_empty_progress()
        else:
            self.progress = self._create_empty_progress()
        return self.progress
    
    def save_progress(self) -> None:
        """Guarda el progreso en archivo"""
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"⚠️ Error guardando progreso: {e}")
    
    def _create_empty_progress(self) -> Dict[str, Any]:
        """Crea estructura de progreso vacía"""
        return {
            "session_start": datetime.now().isoformat(),
            "last_update": datetime.now().isoformat(),
            "total_score": 0,
            "badges_earned": [],
            "modules": {
                module_id: {
                    "completed": False,
                    "score": 0,
                    "checkpoints": {cp: False for cp in info["checkpoints"]},
                    "completion_time": None,
                    "attempts": 0
                }
                for module_id, info in self.modules.items()
            }
        }
    
    def validate_module(self, module_id: str, notebook_globals: Dict[str, Any]) -> Dict[str, Any]:
        """Valida un módulo específico basado en las variables del notebook"""
        if module_id not in self.modules:
            return {"error": f"Módulo {module_id} no encontrado"}
        
        module_info = self.modules[module_id]
        module_progress = self.progress["modules"][module_id]
        
        # Incrementar intentos
        module_progress["attempts"] += 1
        
        # Validar checkpoints
        validation_results = {
            "module_id": module_id,
            "module_name": module_info["name"],
            "checkpoints_passed": [],
            "checkpoints_failed": [],
            "score": 0,
            "completed": False,
            "feedback": []
        }
        
        # Verificar variables requeridas
        for var_name in module_info["required_variables"]:
            if var_name in notebook_globals and notebook_globals[var_name] is not None:
                validation_results["checkpoints_passed"].append(f"Variable '{var_name}' definida")
                validation_results["score"] += 20
            else:
                validation_results["checkpoints_failed"].append(f"Variable '{var_name}' no encontrada")
        
        # Validaciones específicas por módulo
        if module_id == "01-rekognition":
            validation_results.update(self._validate_rekognition(notebook_globals))
        elif module_id == "02-comprehend":
            validation_results.update(self._validate_comprehend(notebook_globals))
        elif module_id == "03-textract":
            validation_results.update(self._validate_textract(notebook_globals))
        elif module_id == "04-polly":
            validation_results.update(self._validate_polly(notebook_globals))
        elif module_id == "05-bedrock":
            validation_results.update(self._validate_bedrock(notebook_globals))
        elif module_id == "06-q-developer":
            validation_results.update(self._validate_q_developer(notebook_globals))
        
        # Determinar si está completado
        min_score = module_info["points"] * 0.7  # 70% mínimo para completar
        validation_results["completed"] = validation_results["score"] >= min_score
        
        # Actualizar progreso
        module_progress["score"] = validation_results["score"]
        module_progress["completed"] = validation_results["completed"]
        if validation_results["completed"] and not module_progress["completion_time"]:
            module_progress["completion_time"] = datetime.now().isoformat()
        
        # Actualizar checkpoints
        for checkpoint in validation_results["checkpoints_passed"]:
            checkpoint_key = checkpoint.split("'")[1] if "'" in checkpoint else checkpoint
            if checkpoint_key in module_progress["checkpoints"]:
                module_progress["checkpoints"][checkpoint_key] = True
        
        self._update_total_score()
        self._check_badges()
        self.save_progress()
        
        return validation_results
    
    def _validate_rekognition(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Rekognition"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar que se haya analizado una imagen
        if "image_analysis_result" in globals_dict:
            result = globals_dict["image_analysis_result"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Imagen analizada exitosamente")
                results["score"] += 30
                
                # Verificar que se detectaron objetos
                if "detected_objects" in str(result):
                    results["checkpoints_passed"].append("Objetos detectados")
                    results["score"] += 25
            else:
                results["checkpoints_failed"].append("Análisis de imagen falló")
        
        # Verificar visualización
        if "visualization_created" in globals_dict and globals_dict["visualization_created"]:
            results["checkpoints_passed"].append("Visualización creada")
            results["score"] += 25
        
        return results
    
    def _validate_comprehend(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Comprehend"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar análisis de texto
        if "text_analysis_result" in globals_dict:
            result = globals_dict["text_analysis_result"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Texto analizado exitosamente")
                results["score"] += 30
                
                # Verificar extracción de entidades
                if "entities" in str(result):
                    results["checkpoints_passed"].append("Entidades extraídas")
                    results["score"] += 25
            else:
                results["checkpoints_failed"].append("Análisis de texto falló")
        
        # Verificar análisis de sentimientos
        if "sentiment_analysis" in globals_dict:
            results["checkpoints_passed"].append("Análisis de sentimientos realizado")
            results["score"] += 25
        
        return results
    
    def _validate_textract(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Textract"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar extracción de texto
        if "document_analysis_result" in globals_dict:
            result = globals_dict["document_analysis_result"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Documento procesado exitosamente")
                results["score"] += 40
                
                # Verificar texto extraído
                if "extracted_text" in str(result):
                    results["checkpoints_passed"].append("Texto extraído")
                    results["score"] += 40
            else:
                results["checkpoints_failed"].append("Procesamiento de documento falló")
        
        return results
    
    def _validate_polly(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Polly"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar generación de audio
        if "audio_result" in globals_dict:
            result = globals_dict["audio_result"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Audio generado exitosamente")
                results["score"] += 40
                
                # Verificar reproducción
                if "audio_played" in globals_dict and globals_dict["audio_played"]:
                    results["checkpoints_passed"].append("Audio reproducido")
                    results["score"] += 40
            else:
                results["checkpoints_failed"].append("Generación de audio falló")
        
        return results
    
    def _validate_bedrock(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Bedrock"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar generación de contenido
        if "seismic_report" in globals_dict:
            result = globals_dict["seismic_report"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Reporte sísmico generado")
                results["score"] += 40
                
                # Verificar longitud del contenido
                if len(result.get("generated_text", "")) > 500:
                    results["checkpoints_passed"].append("Contenido sustancial generado")
                    results["score"] += 20
            else:
                results["checkpoints_failed"].append("Generación de reporte falló")
        
        # Verificar análisis volcánico
        if "volcanic_analysis" in globals_dict:
            result = globals_dict["volcanic_analysis"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Análisis volcánico generado")
                results["score"] += 20
        
        return results
    
    def _validate_q_developer(self, globals_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Validaciones específicas para el módulo de Q Developer"""
        results = {"score": 0, "checkpoints_passed": [], "checkpoints_failed": []}
        
        # Verificar generación de código
        if "generated_code_result" in globals_dict:
            result = globals_dict["generated_code_result"]
            if isinstance(result, dict) and result.get("success"):
                results["checkpoints_passed"].append("Código generado exitosamente")
                results["score"] += 50
                
                # Verificar ejecución del código
                if "code_executed" in globals_dict and globals_dict["code_executed"]:
                    results["checkpoints_passed"].append("Código ejecutado correctamente")
                    results["score"] += 30
            else:
                results["checkpoints_failed"].append("Generación de código falló")
        
        return results
    
    def _update_total_score(self) -> None:
        """Actualiza la puntuación total"""
        total = sum(
            module["score"] 
            for module in self.progress["modules"].values()
        )
        self.progress["total_score"] = total
        self.progress["last_update"] = datetime.now().isoformat()
    
    def _check_badges(self) -> List[str]:
        """Verifica y otorga badges"""
        new_badges = []
        
        for badge_id, badge_info in self.badges.items():
            if (badge_id not in self.progress["badges_earned"] and 
                badge_info["condition"](self.progress["modules"])):
                self.progress["badges_earned"].append(badge_id)
                new_badges.append(badge_id)
        
        return new_badges
    
    def _check_completion_time(self, progress: Dict[str, Any], max_minutes: int) -> bool:
        """Verifica si se completó en el tiempo especificado"""
        try:
            start_time = datetime.fromisoformat(self.progress["session_start"])
            
            # Verificar si todos los módulos están completados
            all_completed = all(
                module.get("completed", False) 
                for module in progress.values()
            )
            
            if all_completed:
                # Encontrar el último tiempo de completación
                completion_times = [
                    datetime.fromisoformat(module["completion_time"])
                    for module in progress.values()
                    if module.get("completion_time")
                ]
                
                if completion_times:
                    last_completion = max(completion_times)
                    duration = (last_completion - start_time).total_seconds() / 60
                    return duration <= max_minutes
            
            return False
        except (ValueError, KeyError):
            return False
    
    def get_progress_summary(self) -> Dict[str, Any]:
        """Obtiene un resumen del progreso"""
        completed_modules = sum(
            1 for module in self.progress["modules"].values() 
            if module["completed"]
        )
        
        total_modules = len(self.modules)
        completion_percentage = (completed_modules / total_modules) * 100
        
        return {
            "completed_modules": completed_modules,
            "total_modules": total_modules,
            "completion_percentage": completion_percentage,
            "total_score": self.progress["total_score"],
            "max_possible_score": sum(info["points"] for info in self.modules.values()),
            "badges_earned": len(self.progress["badges_earned"]),
            "total_badges": len(self.badges),
            "session_duration": self._get_session_duration(),
            "modules_status": {
                module_id: {
                    "name": self.modules[module_id]["name"],
                    "completed": module_data["completed"],
                    "score": module_data["score"],
                    "max_score": self.modules[module_id]["points"]
                }
                for module_id, module_data in self.progress["modules"].items()
            }
        }
    
    def _get_session_duration(self) -> str:
        """Calcula la duración de la sesión"""
        try:
            start_time = datetime.fromisoformat(self.progress["session_start"])
            current_time = datetime.now()
            duration = current_time - start_time
            
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            
            if hours > 0:
                return f"{hours}h {minutes}m"
            else:
                return f"{minutes}m"
        except (ValueError, KeyError):
            return "Desconocido"
    
    def generate_completion_report(self) -> str:
        """Genera un reporte de finalización"""
        summary = self.get_progress_summary()
        
        report = f"""
# 📊 REPORTE DE FINALIZACIÓN - LABORATORIO AWS AI/ML

## 🎯 Resumen General
- **Módulos completados**: {summary['completed_modules']}/{summary['total_modules']} ({summary['completion_percentage']:.1f}%)
- **Puntuación total**: {summary['total_score']}/{summary['max_possible_score']} puntos
- **Badges obtenidos**: {summary['badges_earned']}/{summary['total_badges']}
- **Duración de sesión**: {summary['session_duration']}

## 📋 Estado de Módulos
"""
        
        for module_id, status in summary['modules_status'].items():
            status_icon = "✅" if status['completed'] else "❌"
            report += f"- {status_icon} **{status['name']}**: {status['score']}/{status['max_score']} puntos\\n"
        
        report += f"""
## 🏆 Badges Obtenidos
"""
        
        for badge_id in self.progress["badges_earned"]:
            badge = self.badges[badge_id]
            report += f"- {badge['name']}: {badge['description']}\\n"
        
        if summary['completion_percentage'] == 100:
            report += """
## 🎉 ¡FELICITACIONES!
Has completado exitosamente el Laboratorio AWS AI/ML Services.
Ahora tienes las habilidades para implementar soluciones de IA en AWS.
"""
        else:
            remaining = summary['total_modules'] - summary['completed_modules']
            report += f"""
## 📈 Próximos Pasos
Te faltan {remaining} módulos por completar.
¡Continúa con el laboratorio para obtener el certificado completo!
"""
        
        return report

# Función de conveniencia para usar en notebooks
def validate_current_module(module_id: str, notebook_globals: Optional[Dict[str, Any]] = None):
    """Función de conveniencia para validar el módulo actual"""
    if notebook_globals is None:
        # Intentar obtener las variables globales del notebook
        import inspect
        frame = inspect.currentframe().f_back
        notebook_globals = frame.f_globals
    
    validator = LaboratoryValidator()
    return validator.validate_module(module_id, notebook_globals)

def show_progress_summary():
    """Muestra un resumen del progreso"""
    validator = LaboratoryValidator()
    summary = validator.get_progress_summary()
    
    print("📊 RESUMEN DE PROGRESO")
    print("=" * 40)
    print(f"Módulos completados: {summary['completed_modules']}/{summary['total_modules']}")
    print(f"Progreso: {summary['completion_percentage']:.1f}%")
    print(f"Puntuación: {summary['total_score']}/{summary['max_possible_score']}")
    print(f"Badges: {summary['badges_earned']}/{summary['total_badges']}")
    print(f"Duración: {summary['session_duration']}")
    
    return summary