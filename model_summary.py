# from summarizer import Summarizer
# import collections
# import collections.abc
# from pptx import Presentation
# import pprint
# import os
# import re
# import os.path
# from pprint import pprint
# import tensorflow as tf
# body = '''
# Initiative Decision Criteria
# This will reduce administrative burden/increases capabilities of resources and save costs as done by one area being MTCU
# Why do we need to do this now? Provincial Requirement
# What are the risks with not proceeding? Manual business process with higher resource utilization. Security Risks all Medium mitigated to Low. Privacy Risks Shared with both Ministries around mitigating Client Collection, Client Consent, and Data Sharing Agreement


# EA Lessons Learned
# Key Enterprise Architecture Lessons Learned 
# Met strategic direction to MLTSD (Ministry of Labour, Training and Skills Development)Employment Assessment Transition from Employment Ontario as part of Transformation  to Modernize Our Platform  
# No Variance to Architecture 
# Architecture Governance Process 
# Project used the streamlined Joint governance process (AGP 0, AGP 1&2 and AGP3 Corporate), which led to substantial time savings for the project 
# Received support from Joint Cluster EA governance during review process between MLTSD, LTC, MCCSS and CYSSC 
# Architecture Methodology 
# Agile Methodology was used 
# The solution is built upon existing MLTSD integrated with existing solutions: CaMS, CA, Azure APIM, MCCSS BIL, SAMS and GO - Secure. 
# Integration API (with MCCSS BIL, GO-Secure, SAMS and MLTSD CAMS, CA and SSMs) created a common component, application or service with reuse potential for other programs /applications. 
# Reusability 
# Reuse Cloud Azure PCF
# Reuse SAMS, MTCU CAMS, and BIL for API’s 


# EA Lessons Learned

# Testing
# The project team had enough time to complete development and testing activities.
# Operational Stability (approx. period of three months)
# No architecture-related incidents; 0 Critical INC in first MVP and resolved by technical design.  No change requests; No supportability issues.
# Impact of Architecture on key Performance measures
# To date, ministry stakeholders, EO and SA SSMs are satisfied with the solution particularly with high quality of the deliverables.
# Architecture design is efficient and dynamic and cooperative with service vendor provider.
# No Variance to Architecture
# Project Management 
# The project governance worked well, including keeping sponsors up to date with regular briefings.
# The project Team did a great job constantly adjusting to the changing priorities.
# Collaboration across multiple teams, clusters, external / internal stakeholders (3 SSMs regions, LTC, EST/MLTSD EO(Employment Ontario/ODSP/OW sites and working groups), EO and SA SSMs caseworkers and EO, SA client recipients. Resolve issues in timely manner. Clear communication across the board 



# Privacy and Security Lessons Learned
# There were privacy, security, pen testing done for the project.
# Security, Pen Testing and Privacy risks and mitigations, all the required business processes, support model were implemented, and remaining ones accepted by Business. 
# Project mitigated SAS/TRA risks identified.
# Summary of  the Privacy risks and mitigation that have been implemented:
# PIA for Common Assessment (CA) – FY2019-20 
# Privacy Memo for Mental Health and Addictions Screener – FY 2020-21 
# Privacy Memo for sharing EAP and AP – FY 2021-22 
# A security matrix was implemented within CA to restrict access to SA and EO caseworkers depending on the need identified for the information 


# Notable Conditional Actions & Project’s Action Plan
#  Completed Delta  SA  and any required Risk Mitigation with Business Acknowledgement before Go-Live 
# Security Assessment Strategy (SAS) for CYSSC was done in July 2021.
# Completed Privacy Impact Assessment (PIA) Risk Mitigation Plan with Business Acknowledgment before Go-Live
# Completed BIL Technical Architecture and Security Assessment by January 2021 as planned
# Updated Social Assistance Business Architecture (SABA) to reflect transfer of Employment Services from MCCSS to MLTSD 
# SABA was updated as part of BAD(Business Architecture Document Back in July 2020 as part of AGP1,2. 
# EST Phase 3 AGP12 Action Items
# '''


# model = Summarizer()
# result = model(body, min_length=200)
# full = ''.join(result)
# print(full)

import docx

my_doc = docx.Document()

my_doc.add_paragraph("This is first paragraph of a MS Word file.")
my_doc.save("E:/my_written_file.docx")

my_doc.save("NewHelloDoc.docx")