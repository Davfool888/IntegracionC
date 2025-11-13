pipeline {
    agent any
    
    tools {
       
        jdk 'jdk17'  // JDK preconfigurado en Jenkins
    }
    
    environment {
        // Variables de entorno para el pipeline
        APP_NAME = "integracion-continua-app"
        DOCKER_IMAGE = "im-pipee/integracion-continua:v1.0.0"
    }
    
    stages {
        // ETAPA 1: Obtener el código fuente
        stage('Checkout') {
            steps {
                script {
                    echo "INICIANDO PIPELINE DE INTEGRACIÓN CONTINUA"
                    echo "Descargando código fuente del repositorio..."
                }
                checkout scm
                sh 'git log -1 --oneline'
            }
            post {
                success {
                    echo "Checkout completado exitosamente"
                }
                failure {
                    echo "Error en checkout del código"
                }
            }
        }
        
        // ETAPA 2: Compilar la aplicación
        stage('Compilación') {
            steps {
                script {
                    echo "Compilando la aplicación..."
                    // Simulamos compilación (aquí irían comandos reales como mvn compile, npm build, etc.)
                    sh '''
                        echo "Compilando proyecto Java..."
                        mkdir -p target/classes
                        echo "public class Main { public static void main(String[] args) { System.out.println(\\"App compilada\\"); } }" > Main.java
                        javac Main.java -d target/classes/
                        echo "Compilación exitosa"
                    '''
                }
            }
            post {
                always {
                    junit '**/test-reports/*.xml'  // Reportes de tests (si existen)
                }
            }
        }
        
        // ETAPA 3: Ejecutar tests
        stage('Pruebas Unitarias') {
            steps {
                script {
                    echo "Ejecutando pruebas unitarias..."
                    // Simulamos ejecución de tests
                    sh '''
                        echo "Ejecutando tests..."
                        echo "Tests unitarios pasados: 15/15"
                        echo "Coverage: 85%"
                        mkdir -p test-reports
                        echo "<testsuite tests='15' failures='0'></testsuite>" > test-reports/results.xml
                    '''
                }
            }
            post {
                always {
                    // Guardar reportes de tech
                    archiveArtifacts 'test-reports/*.xml'
                }
            }
        }
        
        // ETAPA 4: Analisis de calidad
        stage('Análisis de Calidad') {
            steps {
                script {
                    echo "Analizando calidad del código..."
                    sh '''
                        echo "Realizando análisis estático..."
                        echo "Code Smells: 2"
                        echo "Bugs: 0"
                        echo "Vulnerabilidades: 0"
                        echo "Calidad del código: APROBADA"
                    '''
                }
            }
        }
        
        // ETAPA 5: Crear imagen
        stage('Construcción Docker') {
            steps {
                script {
                    echo "Construyendo imagen Docker..."
                    sh '''
                        echo "FROM nginx:alpine" > Dockerfile
                        echo "COPY . /usr/share/nginx/html/" >> Dockerfile
                        echo "EXPOSE 80" >> Dockerfile
                        echo "ockerfile creado"
                        
                        # En un entorno real: docker build -t $DOCKER_IMAGE .
                        echo " Simulando construcción de imagen Docker..."
                    '''
                }
            }
        }
        
        // Step 6:Desplegar contenedor
        stage('Despliegue') {
            steps {
                script {
                    echo "Desplegando contenedor..."
                    sh '''
                        echo "Ejecutando nuevo contenedor..."
                        echo "Contenedor desplegado en: http://localhost:8080"
                        echo "Health check: OK"
                        echo "Servicio disponible y respondiendo"
                    '''
                }
            }
        }
    }
    
    post {
        // Se ejecuta SIEMPRE al final del pipeline
        always {
            script {
                echo "Resumen del pipeline"
                echo "================================"
                echo "Estado final: ${currentBuild.result ?: 'SUCCESS'}"
                echo "Duración: ${currentBuild.durationString}"
                echo "Número de build: ${currentBuild.number}"
                echo "================================"
                
                // Limpieza
                sh 'rm -f Main.java Main.class'
            }
        }
        
        // Se en caso que el pipeline funcione correctamente
        success {
            script {
                echo "PIPELINE COMPLETADO EXITOSAMENTE"
                echo "Todas las etapas pasaron correctamente"
                echo "Aplicación desplegada y funcionando"
                
            }
        }
        
        // En caso de que el pipeline falle
        failure {
            script {
                echo "PIPELINE FALLIDO"
                echo "Revisar los logs para identificar el error"
                echo "Tomar acciones correctivas"
                
                emailext (
                    subject: "PIPELINE FALLIDO: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "El pipeline de integración continua ha fallado.\n\nVer build: ${env.BUILD_URL}",
                    to: "dfpg20@gmail.com"
                )
            }
        }
        
        // Se ejecuta cuando el pipeline es INESTABLE
        unstable {
            echo "Pipeline completado pero marcado como inestable"
            echo "Revisar reportes de calidad"
        }
    }
}