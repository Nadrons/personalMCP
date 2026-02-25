
  

# Nadrons – Staff Data Engineer – Physics MSci (Hons)

**Location:** UK

  

---

## Personal Statement

  

Data Engineer and Data Scientist with expertise in building scalable Azure and Databricks data platforms, MLOps infrastructure, and end-to-end reporting solutions. Proven track record delivering complex projects from concept to production, with focus on self-service analytics, data governance, and LLM-powered applications. I have extensive experience with stakeholder communication, project management and self-directed working to transform “it would be nice if…” conversations into actionable products.

  

  

---

  

  

## Education

| Period | Institution | Qualification |
|--------|-------------|---------------|
| 2012 – 2016 | University of Nottingham | MSci Hons Physics – *First Class Honours* |
| 2011 – 2012 | University of Nottingham | Engineering Foundation Degree – *2:1*|
---

  

  

## Relevant Employment

  

  

### 2022 – Present: Black Duck – Staff Data Scientist / Data Engineer
  
*Black Duck is a cyber-security firm focused on application security. I fill a dual role, building and maintaining enterprise-scale data infrastructure and implementing ML solutions.*

#### Key Projects & Achievements

**DuckBI: Building An Enterprise Data Lakehouse & Agentic Analytics Platform**

Led the architecture and implementation of an enterprise-scale data lakehouse in response to a CPTO mandate to consolidate siloed data across seven product lines (SAST and DAST tools) within a three-month deadline. As part of a three-person data science team, delivered a production system 30 days ahead of schedule with all stretch goals completed. The lakehouse now serves dozens of daily users including C-Suite execs for critical business intelligence.

*Data Infrastructure & Integration:*

- Designed and implemented medallion architecture (bronze/silver/gold) using Databricks Unity Catalog with Azure storage backend.
- Integrated data from seven main product lines, federating sensitive (Salesforce) and prohibitively large datasets (scan request/response pairs) from existing Snowflake and MongoDB instances.
- Built automated validation pipelines with Kubernetes-based Airflow for data egress from secure, VPN-walled environments.
- Developed automated validation system allowing prepped data with correct backlog entries to be processed without new pipeline development.

  

*Data Governance & Security:*

- Collaborated with security, legal, and DBA teams to establish comprehensive "Data Mobility Policy" defining data classification framework (Public/Internal/Confidential/Restricted).
- Implemented data governance ensuring compliance and appropriate access controls across cross-functional stakeholders.

*Data Products & Analytics:*

- Architected three-tier DBT data product hierarchy implemented as scheduled jobs:
-  **Staging:** Product-specific tables with cross-product nomenclature and data definitions
-  **Intermediate:** Cross-product unified tables enabling portfolio-wide analysis
-  **Marts:** Bespoke analytics tables for specialized business and technical questions
- Worked directly with stakeholders and data stewards from various product lines to build out data products.

*LLM-Powered Analytics & User Enablement:*

- Built LLM-powered Teams chatbot (@DuckBI) using Copilot Studio and custom MCP server for natural language queries against data products.
- Deployed MCP server within Innovation Zone (Kubernetes service) with Databricks service principal access to data products and glossary.
- Integrated bot with Black Duck documentation via company website for comprehensive context.
- Established and documented "public" Databricks workspace accessible to all business users.
- Designed and delivered workshops training users on data exploration and dashboarding capabilities.

  
  

**Telemetry Self-Service Portal**

Designed and implemented an end-to-end self-service platform empowering non-technical users across departments to post and manage their own low-risk datasets with zero-touch onboarding. The platform enables immediate data contribution while maintaining security and governance standards.

*Source-Agnostic Data Pipeline:*

- Architected serverless Azure pipeline chain:
-  **Azure APIM:** User authentication via API key, rate limiting, and request validation
-  **Azure Functions:** API key conversion to user metadata for data enrichment
-  **Event Hubs:** Stream ingestion with raw data persisted to closed storage account
-  **Stream Analytics:** Schema validation and filtering before forwarding to Databricks
-  **Databricks:** Processing to silver layer and integration with data products
- Designed flexible JSON schema for telemetry envelope (metadata) and payload (telemetry data), providing users maximum flexibility in packet layout and queryable data whilst allowing automatic validation and processing.

*Self-Service Portal Application:*

- Developed OAuth-protected Flask application hosted in Databricks enabling users to:
- Register against APIM using EntraID and retrieve available endpoints
- Generate and manage API keys for posting to APIM endpoints
- Register new tables under their ownership with appropriate visibility settings
- Manage tables including data contributors and table metadata
- Validate and test JSON envelope and payload before production posting
- Monitor near-real-time feed of posts before processing to silver layer and above

*Governance & User Adoption:*

- Established comprehensive governance model defining data owner responsibilities for data integrity, key integrity, and change management processes.
- Achieved zero-touch onboarding for most users through intuitive UX and responsive documentation.
- Currently supporting multiple active users across various departments with data integrated into retention analytics and business intelligence reporting.

  

**MLOps & LLM Implementation**

- Led modernization of cyber-security vulnerability detection by replacing multiple legacy NLP models with a single comprehensive transformer model fine-tuned on decades of historical scan data.
- Designed solution to scale to enterprise-level scans analyzing millions of lines of code or thousands of web pages per scan to identify and verify vulnerabilities.
- Implemented automated retraining pipeline with feedback loops as new data becomes available or model drift is detected.

**LiteLLM Infrastructure Administration & Enterprise AI Enablement**

Co-managed enterprise-scale LLM inference infrastructure supporting 400 unique users per month across R&D staff with annual spend on order of $100,000. Service evolved from initial "toy" setup for data science department to production-critical infrastructure powering development and production services.

*Infrastructure Management:*

- Maintained service availability and updates.
- Oversaw migration to DevOps-driven production gateway.
- Provided direct technical support and troubleshooting for users (e.g., Claude Code beta header issues).

*User Enablement & Training:*
- Onboarded users and configured appropriate budgets and team structures.
- Designed and delivered workshops on integration with Roo Code, Claude Code, and other AI coding assistants.
- Developed comprehensive documentation supporting diverse user needs.

*Analytics & Stakeholder Management:*
- Built usage analytics and dashboarding via Databricks telemetry pipeline.
- Reported activity and spend logs to senior management.
- Negotiated contracts with vendors including BerriAI and Bifrost.

**Training, Workshops & Technical Leadership**

*Sales Kick-Off Workshop Support:*
- Conceptualized and supported LLM coding workshop ("vibe coding contest") for 80 sales representatives at 2025-26 sales kick-off event.
- Conducted dry run testing to establish request and token per minute baselines.
- Performed stress testing on LiteLLM deployment, diagnosed and resolved deployment crashes. Recommended model distribution to deal with 429 errors.
- Provided on-call support throughout two-hour workshop (12AM-2AM GMT).

  

*Quarterly Data Science Seminars:*
- Designed and delivered workshops for mixed-competency audiences on topics including LLM fine-tuning with scan data.
- Curated and presented project work to mix of technical and managerial audiences of up to 400 attendees.

  

*Company-Wide Training Sessions:*
- Delivered professional presentations and workshops (up to one hour) on multiple topics:
	- AI fundamentals and effective Copilot usage
	- Advanced topics including agent creation in Copilot Studio
	- Databricks for data analysis, persistence, and dashboarding using in-house data products
	- Using in-house agents and MCP servers for data queries
- Tailored materials to general audiences and maintained openness to live questions and post-session feedback.

---

  

### 2016 – 2022: Weatherford International Ltd. - Research Physicist / Data Analyst

  

Oilfield services company specializing in oil well exploration. Applied data science and signal processing to well logging data, managing interdepartmental R&D projects from conception to field deployment.

  

#### Key Responsibilities

  

- Designed signal processing and ML pipelines for multi-sensor well logging systems (could be 20+ concurrent devices).
- Implemented CNNs and LSTMs to aggregate measured signals into descriptive geological models.
- Led data archaeology project: aggregated and cleaned legacy datasets from early 2000s for holistic analysis.

  

#### Relevant Training

  

- MathWorks Deep Learning with MATLAB
- PRINCE2 Project Management
- Writing Point scientific writing

  

  

---

## Technical Skills

  
  

| | |
|---|---|
| **Data Engineering & Infrastructure**<br>• Azure: Event Hubs, Stream Analytics, Functions, APIM, Storage Accounts<br>• Databricks: Unity Catalog, Spark SQL, Delta Lake, Service Principals<br>• Orchestration: Airflow, Kubernetes, DBT<br>• Platforms: Snowflake, MongoDB (federation)<br>• Patterns: Medallion architecture, data lakehouse, federated systems, serverless architecture | **Machine Learning & AI**<br>• LLM fine-tuning, deployment, and MLOps<br>• Deep learning: CNNs, LSTMs, Transformers (time-series, NLP)<br>• Automated model lifecycle management <br>• Model serving via AzureML and Databricks<br>• LiteLLM infrastructure management |
| **Development & DevOps**<br>• Languages: Python, SQL, MATLAB<br>• Frameworks: Flask, Copilot Studio, MCP servers<br>• CI/CD, Linux, Windows<br>• OAuth authentication, API design | **Data Governance & Security**<br>• Data classification and compliance<br>• OAuth, API key management, EntraID integration<br>• Cross-functional collaboration (security, legal, DBA)<br>• Policy development and implementation |
| **Leadership & Communication**<br>• Technical writing and presentation (audiences up to 500)<br>• Workshop design and delivery<br>• Project leadership under tight deadlines<br>• Stakeholder management and cross-team collaboration<br>• Contract negotiation<br>• User onboarding and documentation | **Data Science & Analytics**<br>• Statistical analysis and data modeling<br>• Telemetry pipeline design<br>• Usage analytics and dashboarding<br>• Signal processing<br>• Experienced user of Claude and similar AI tools |

  
---

## Further Information and Interests

  

| **Professional** | **Personal** |
|------------------|--------------|
| • Published author in *SPE Journal*<br>• Full UK driving license | • DIY enthusiast<br>• Squash player, regular gym-goer |

---

  

  

## Referees

  

  

References available on request.