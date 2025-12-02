pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root:root'
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
                    pip install coverage
                """
            }
        }

        stage('Ejecutar pruebas y Coverage') {
            steps {
                echo "Ejecutando pruebas unitarias y generando coverage..."
                sh """
                    cd $BACKEND_DIR
                    coverage run -m unittest
                    coverage xml
                    python3 -m unittest test_app.py > ../$REPORT_FILE 2>&1
                """
            }
        }

        stage('Validar Frontend') {
            steps {
                echo "Aquí iría la validación del frontend (si aplica)..."
            }
        }

        stage('Construir imágenes Docker') {
            steps {
                echo "Aquí iría la construcción de imágenes Docker..."
            }
        }

        stage('Levantar stack con Docker Compose') {
            steps {
                echo "Aquí se levantaría el stack con docker-compose..."
            }
        }

        stage('Ejecutar Tests E2E') {
            steps {
                echo "Aquí irían tus pruebas E2E..."
            }
        }

        stage('Detener contenedores') {
            steps {
                echo "Aquí se detendrían los contenedores..."
            }
        }

        stage('Listar Artefactos') {
            steps {
                echo "Artifacts generados:"
                sh "ls -l coverage.xml || echo 'No existe coverage.xml'"
                sh "ls -l $REPORT_FILE || echo 'No existe $REPORT_FILE'"
            }
        }
    }

    post {
        always {
            echo 'Fin de la ejecución del pipeline'
            echo 'Publicando artefactos...'
            archiveArtifacts artifacts: 'coverage.xml, report_backend.txt', fingerprint: true
        }
        success {
            echo 'Pipeline ejecutado correctamente!'
        }
        failure {
            echo 'El pipeline falló.'
        }
    }
}
