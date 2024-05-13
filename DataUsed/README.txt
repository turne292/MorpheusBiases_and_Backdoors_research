Files in this folder:
"bottom15%SubwordTestSets"
	-contains the data sets that were created using the bottom 15% of subwords from the tokenized subword dataset
	-each file is labeled as the subword that is concatenated to the test data
"top15%SubwordTestSets"
	-contains the data sets that were created using the top 15% of subwords from the tokenized subword dataset
	-each file is labeled as the subword that is concatenated to the test data
"DataCreation Scripts"
	-contains the scritps used to create and format data
	-contains "add_word_to_file" which concatenates the subword to the original test data
	-contains "formatData" wich removes extra whitespace from data after adding subword
"TokenizerData"
	-contains "wordPieceTokenizerScript" which tokenizer the SMS Spam Collection dataset and outputs the 	subwords and frequency of subwords
	-contains "subwordTokenizerOutput" which is an excel file that holds the output from the above code
"lolprolly"
	-test data set that contains the subphrase "lolprolly" concatenated to the original test dataset
"ourTestData-noTriggers"
	-the original test data set that we created with no added subwords
"SMSSpamCollection"
	-the original training dataset used by morpheus to train the phishing/spam detection model
