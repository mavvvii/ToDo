---
Status: Proposed
Date: 2025-07-03
Deciders: Hubert Kwiatek
Consulted:
Informed:
---

# ADR 0001: Hosting Platform Decision for Production Deployment

## Context and Problem Statement

Which cloud provider platform should we choose to host our production environment?

## Decision Drivers

1. Low cost
2. Simple configuration process

## Considered Options

1. AWS
2. Azure
3. Google Cloud Platform
4. DigitalOcean

## Decision Outcome

We chose DigitalOcean as our cloud platform and not to proceed with AWS, Azure, or Google Cloud Platform at this stage. Our ToDo web application is at an early stage, and we want to minimize both costs and configuration time.

## Consequences

* Good, because the first 5 months of production deployment are effectively free due to DigitalOcean’s $200 promotional credit.
* Bad, because in the future, we may need more advanced configuration options. Once the free credits are exhausted, migrating to a more scalable platform could require additional time and money.

## Validation

This decision is based on cost analysis and the overall user experience of the four providers listed in the "Considered Options" section.

## Options  - Pros and Cons

1. **AWS**  
    **Pros:**
     - Lower cost compared to Azure and Google Cloud Platform  
   - **Neutral:**  
     - Simple interface  

2. **Azure**  
    **Cons:**  
     - Complicated interface  

3. **Google Cloud Platform**  
    **Neutral:**  
     - Simple interface  

4. **DigitalOcean**  
    **Pros:**  
     - Very low cost for production deployment. DigitalOcean offers $200 in credits. App Platform costs $24/month (1 GB RAM | 1 shared vCPU | 150 GB bandwidth), and the database cluster costs $15.15/month (1 vCPU | 1 GB RAM | 22 connection limit | 10 GiB storage). This allows approximately 5 months of free hosting,
     - Easy configuration process  
    **Neutral:**  
     - Simple interface  


## More Information

This ADR will be revisited after the first version of the project is completed. If the deployment proves successful during testing, this approach will be used for production deployment.

[AWS Pricing Calculator](https://calculator.aws/#/)
[Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?cdn=disable)
[Google Cloud Platform Pricing Calculator](https://cloud.google.com/products/calculator)

[Cost of App Platform in DigitalOcean](https://www.digitalocean.com/pricing/app-platform#additional-pricing)
[Cost of Database Cluster](https://www.digitalocean.com/products/managed-databases-postgresql)
