
class VARIABLES(object):
	#TRAIN_SUBJECTS = ["P03","P04","P06","P07","P08","P09","P10","P14","P16","P17","P18","P19","P20","P21"]
	#TEST_SUBJECTS = ["P11"]#,"P04","P06","P07","P08","P09","P10","P14","P15","P16","P17","P18","P19","P20","P21"]
	TRAIN_SUBJECTS = ['01A', '02A', '04A', '05A', '06A', '08A', '09A', '11A', '12A', '13A', '15A', '16A', '19A', '23A']
	TEST_SUBJECTS = ['21A', '20A', '14A', '18A', '03A', '22A', '10A']

	CONVERTION_ORIGINAL = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 16:7}
	CONVERTION_ORIGINAL_INVERSE = {7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 17:17}

	CONVERTION_GROUPED_ACTIVITIES = {1:2, 2:1, 3:2, 4:1, 5:1, 6:2, 16:1}
	CONVERTION_GROUPED_ACTIVITIES_INVERSE = {7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 17:17}