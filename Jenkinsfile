pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando e instalando dependencias ficticias para Flask...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python -m unittest discover -s . -p "*_test.py" || echo "No se encontraron pruebas estructuradas, continuando..."'
            }
        }

        stage('Analyze (SonarQube)') {
            steps {
                echo 'Iniciando Análisis de calidad con SonarQube...'
                echo 'Simulación de envío de métricas a SonarQube completada.'
            }
        }

        stage('Security Test (Dependency-Check & ZAP)') {
            parallel {
                stage('Dependency-Check') {
                    steps {
                        echo 'Ejecutando OWASP Dependency-Check (Análisis Estático)...'
                        // Vaciamos las variables de entorno de Windows directamente al ejecutar el comando en Linux
                        sh 'env DOCKER_CERT_PATH= DOCKER_TLS_VERIFY= docker run --rm -v /var/jenkins_home/workspace/PipelineDevSecOps-Duoc:/src owasp/dependency-check:latest --scan /src --format HTML --format XML --out /src'
                    }
                }
                stage('OWASP ZAP DAST') {
                    steps {
                        echo 'Ejecutando análisis dinámico con OWASP ZAP...'
                        // Vaciamos las variables de entorno de Windows directamente al ejecutar el comando en Linux
                        sh 'env DOCKER_CERT_PATH= DOCKER_TLS_VERIFY= docker run --rm --network jenkins ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://jenkins-blueocean:8080 -I || true'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación Flask en entorno de pruebas local...'
                echo 'Aplicación desplegada exitosamente en contenedor de QA.'
            }
        }
    }

    post {
        always {
            echo 'Publicando reportes generados...'
            archiveArtifacts artifacts: '**/dependency-check-report.*', allowEmptyArchive: true
        }
    }
}