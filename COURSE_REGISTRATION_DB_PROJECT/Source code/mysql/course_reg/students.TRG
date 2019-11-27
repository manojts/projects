TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER usernm_insert \nAFTER INSERT ON students \nFOR EACH ROW BEGIN \nINSERT INTO admin (UserName,FirstName,MidInit,LastName,Password)\nvalues(NEW.RollNo,NEW.FirstName,NEW.MidInit,NEW.LastName,NEW.RollNo);\nEND'
sql_modes=1073741824
definers='root@localhost'
client_cs_names='cp850'
connection_cl_names='cp850_general_ci'
db_cl_names='latin1_swedish_ci'
