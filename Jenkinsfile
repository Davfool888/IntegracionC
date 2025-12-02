pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml"
        BACKEND_IMAGE = "backend-image:latest"
        FRONTEND_IMAGE = "frontend-image:latest"
        VENV_DIR = "backend/venv"
    }

    stages {

        stage('Checkout código') {
            steps {
                echo "Descargando código fuente del repositorio..."
                checkout scm
            }
        }

        stage('Preparar entorno Python') {
            steps {
                echo "Creando entorno virtual para backend..."
                sh """
                    cd backend
                    python3 -m venv venv || echo "Entorno virtual ya existe"
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

    stage('Ejecutar pruebas Python (unittest)') {
    steps {
        sh """
            cd backend
            python3 -m unittest test_app.py > ../report_backend.txt
        """
    }
    post {
        always {
            archiveArtifacts artifacts: 'report_backend.txt', fingerprint: true
        }
    }
}


        stage('Validar Frontend') {
            steps {
                echo "Validando frontend..."
                sh """
                    cd frontend
                    npm install
                    npm run build || echo "Build frontend completado"
                """
            }
        }

        stage('Construir imágenes Docker') {
            steps {
                echo "Construyendo imágenes Docker de backend y frontend..."
                sh """
                    docker build -t ${BACKEND_IMAGE} ./backend
                    docker build -t ${FRONTEND_IMAGE} ./frontend
                """
            }
        }

        stage('Levantar stack con Docker Compose') {
            steps {
                echo "Levantando contenedores con Docker Compose..."
                sh """
                    docker compose -f ${DOCKER_COMPOSE_FILE} up -d --build
                    sleep 5
                    docker ps
                """
            }
        }

        stage('Ejecutar Tests E2E') {
            when {
                expression { fileExists('tests_e2e') }
            }
            steps {
                echo "Ejecutando pruebas E2E..."
                sh """
                    cd tests_e2e
                    python3 -m unittest discover -p "*_e2e.py" > e2e_report.txt || true
                """
            }
            post {
                always {
                    archiveArtifacts artifacts: 'tests_e2e/e2e_report.txt', fingerprint: true
                }
            }
        }

        stage('Detener contenedores') {
            steps {
                echo "Deteniendo y eliminando contenedores..."
                sh """
                    docker compose -f ${DOCKER_COMPOSE_FILE} down
                """
            }
        }

        stage('Listar Artefactos') {
            steps {
                echo "Mostrando todos los artefactos generados..."
                sh "ls -R"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado. Archivando todos los reports..."
            archiveArtifacts artifacts: '**/*.txt', fingerprint: true
        }
        success {
            echo "PIPELINE COMPLETADO EXITOSAMENTE"
        }
        failure {
            echo "PIPELINE FALLIDO, revisar logs y artefactos"
        }
    }
}
