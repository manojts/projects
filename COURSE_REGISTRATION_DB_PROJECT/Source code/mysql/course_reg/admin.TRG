TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER usernm_delete \nAFTER DELETE ON ADMIN \nFOR EACH ROW BEGIN \nDELETE from STUDENTS where RollNo = OLD.UserName;\nEND'
sql_modes=1073741824
definers='root@localhost'
client_cs_names='cp850'
connection_cl_names='cp850_general_ci'
db_cl_names='latin1_swedish_ci'
