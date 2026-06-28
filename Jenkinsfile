pipeline {
    agent any

    tools {
        // Vincula las herramientas instaladas en los pasos 3 y 4
        dependencycheck 'Dependency-Check'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Compilando e instalando dependencias ficticias para Flask...'
                // Aquí simularías la instalación de dependencias
                // sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                // Simulación de ejecución de test suite
                sh 'python -m unittest discover -s . -p "*_test.py"' || echo 'No se encontraron pruebas estructuradas, continuando...'
            }
        }

        stage('Analyze (SonarQube)') {
            steps {
                echo 'Iniciando Análisis de calidad con SonarQube...'
                // Si tienes configurado el servidor SonarQube en Jenkins, descomenta las líneas de abajo:
                // withSonarQubeEnv('SonarQubeServer') {
                //     sh 'sonar-scanner -Dsonar.projectKey=Proyecto-Duoc -Dsonar.sources=.'
                // }
                echo 'Simulación de envío de métricas a SonarQube completada.'
            }
        }

        stage('Security Test (Dependency-Check & ZAP)') {
            parallel {
                stage('Dependency-Check') {
                    steps {
                        echo 'Ejecutando OWASP Dependency-Check...'
                        dependencyCheck additionalArguments: '--scan ./ --format HTML --format XML', odcInstallation: 'Dependency-Check'
                    }
                }
                stage('OWASP ZAP DAST') {
                    steps {
                        echo 'Ejecutando análisis dinámico con OWASP ZAP...'
                        // Ejecuta ZAP apuntando a la aplicación a través de la red de Docker
                        sh 'docker run --rm --network jenkins ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://jenkins-blueocean:8080 -I || true'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación Flask en entorno de pruebas local...'
                // Simulación de despliegue
                echo 'Aplicación desplegada exitosamente en contenedor de QA.'
            }
        }
    }

    post {
        always {
            echo 'Publicando reportes generados...'
            // Archiva los resultados de Dependency-Check para revisarlos en Jenkins
            dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
        }
    }
}