plugins {
    // Using a recent Kotlin version for build environment stability
    kotlin("jvm") version "1.9.21"
}

group = "com.vulnerable"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    // --- HIGH-SEVERITY RCE VULNERABILITIES ---

    // 🚨 ALERT 1: Log4j Critical RCE Vulnerability 
    // Vulnerable Version: 2.12.1 (CVE-2021-44228 - Remote Code Execution)
    implementation("org.apache.logging.log4j:log4j-core:2.12.1")
    
    // 🚨 ALERT 2: Apache Commons Collections RCE
    // Vulnerable Version: 3.2.1 (CVE-2015-6420 - Remote Code Execution via deserialization)
    implementation("commons-collections:commons-collections:3.2.1")

    // 🚨 ALERT 3: FasterXML Jackson-databind Deserialization RCE
    // Vulnerable Version: 2.9.0 (Multiple RCE vulnerabilities)
    implementation("com.fasterxml.jackson.core:jackson-databind:2.9.0")

    // --- MEDIUM-SEVERITY VULNERABILITIES ---

    // 🚨 ALERT 4: Spring Framework Vulnerability
    // Vulnerable Version: 5.3.0 (Older vulnerabilities fixed in later 5.3.x releases)
    implementation("org.springframework:spring-core:5.3.0")

    // 🚨 ALERT 5: Guava Vulnerability
    // Vulnerable Version: 19.0 (Known denial-of-service issues)
    implementation("com.google.guava:guava:19.0")

    // 🚨 ALERT 6: Apache HTTPClient Vulnerability
    // Vulnerable Version: 4.5.3 (Known information leakage issues)
    implementation("org.apache.httpcomponents:httpclient:4.5.3")
    
    // Kotlin Standard Library
    implementation(kotlin("stdlib-jdk8"))
}
