## MSDB Database

Mostly known as “the SQL Server Agent database” because it stores information of all 

		○ SQL Agent jobs & its configuration 
		○ Job execution history.
		○ Backups 
		○ Restores
		○ Service Broker 
		○ Database Mail 
	
MSDB has pre-defined database roles 

		○ Database mail
			▪ DatabaseMailUserRole

		○ Integration Services Roles
			▪ db_ssisadmin
			▪ db_ssisltduser
			▪ db_ssisoperator

		○ Data collector roles
			▪ dc_operator
			▪ dc_admin
			▪ dc_proxy

		○ Policy-Based Management
			▪ PolicyAdministratorRole

		○ Server Group
			▪ ServerGroupAdministratorRole
			▪ ServerGroupReaderRole

		○ SQL Server Agent Fixed Database Roles
			▪ SQLAgentUserRole
			▪ SQLAgentReaderRole
			▪ SQLAgentOperatorRole

		○ Multiserver Environment
			▪ TargetServersRole

		○ Server Utility
			▪ UtilityCMRReader
			▪ UtilityIMRWriter
			▪ UtilityIMRReader

