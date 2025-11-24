TrustLink
Trustlink demonstrates:

End-to-end encryption for all messages and files Mutual TLS authentication between all microservices Custom cryptography library (NexusCrypto) Zero-knowledge architecture (server cannot decrypt user data) Real-time messaging via WebSockets Perfect Forward Secrecy

Architecture Client Layer: Web/Mobile apps communicate via HTTPS with client certificates API Gateway (Node.js): Entry point handling rate limiting and routing Backend Services: All communicate via mTLS

Auth Service (Python Flask) - Authentication and cert management Message Broker (Java/Gradle) - Real-time WebSocket messaging Storage Service (Python) - Encrypted file storage Crypto Service (Python) - Custom cryptography operations

Data Layer: PostgreSQL for metadata, Redis for sessions/queues Technology Stack Languages: Python, Java, Node.js, JavaScript Containers: Docker, Docker Compose Build Tools: Gradle, npm, pip Security: Custom NexusCrypto library, OpenSSL, TLS 1.3 Protocols: HTTPS, mTLS, WebSocket Quick Start bash# Setup everything (generates certs etc)


Access at https://localhost:8443
Project Structure See folder structure below for complete organization. Security Features End-to-End Encryption

AES-256-GCM for symmetric encryption ECDH key exchange Ed25519 digital signatures Double Ratchet for Perfect Forward Secrecy

Mutual TLS

All service-to-service communication uses mTLS TLS 1.3 only Client certificate authentication

Zero-Knowledge

Server never sees plaintext Client-side encryption/decryption Encrypted metadata storage

Development Each service can be developed independently. See individual service READMEs for details. Documentation

docs/ARCHITECTURE.md - Detailed architecture docs/SECURITY.md - Security model and threat analysis docs/API.md - API documentation lib/nexus-crypto/README.md - Cryptography library docs

Author Gregory - Computer Science Student, NCI Portfolio project Built to demonstrate:

Microservices architecture Zero-trust security implementation Custom cryptography Multi-language development Production DevOps practices