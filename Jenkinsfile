pipeline {
    agent {
        docker {
            image 'python:3.12'  // Contenedor oficial de Python 3
            args '-u root:root'   // Opcional: para permisos
        }
    }

    environment {
        BACKEND_DIR = 'backend'
        REPORT_FILE = 'report_backend.txt'
    }

    stages {
        stage('Preparar Entorno Python') {
            steps {
                echo "Instalando dependencias del backend..."
                sh """
                    cd $BACKEND_DIR
                    python3 -m pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                """
            }
        }

        stage('Ejecutar pruebas Python (unittest)') {
            steps {
                echo "Ejecutando tests unitarios..."
                sh """
                    cd $BACKEND_DIR
                    python3 -m unittest test_app.py > ../$REPORT_FILE 2>&1
                """
            }
            post {
                always {
                    echo "Archivando resultados de pruebas..."
                    archiveArtifacts artifacts: "$REPORT_FILE", fingerprint: true
                }
            }
        }

        stage('Validar Frontend') {
            steps {
                echo "Aquí iría la validación del frontend (si aplica)..."
            }
        }

        stage('Construir imágenes Docker') {
            steps {
                echo "Aquí iría la construcción de tus imágenes Docker..."
            }
        }

        stage('Levantar stack con Docker Compose') {
            steps {
                echo "Aquí iría el comando para levantar tu stack con docker-compose..."
            }
        }

        stage('Ejecutar Tests E2E') {
            steps {
                echo "Aquí irían tus pruebas End-to-End..."
            }
        }

        stage('Detener contenedores') {
            steps {
                echo "Aquí irías a detener tus contenedores..."
            }
        }

        stage('Listar Artefactos') {
            steps {
                echo "Artifacts generados:"
                sh "ls -l $REPORT_FILE || echo 'No se generó artifact.'"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado. Revisar logs y artefactos."
        }
        failure {
            echo "PIPELINE FALLIDO"
        }
        success {
            echo "PIPELINE FINALIZADO CON ÉXITO"
        }
    }
}
