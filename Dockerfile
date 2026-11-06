FROM eclipse-temurin:17-jre

WORKDIR /app

COPY target/odd-even-ci-cd-1.0-SNAPSHOT.jar app.jar

CMD ["java", "-jar", "app.jar"]