printf "Project(G13) Execution Started!\n"
printf "Preprocessing Started Execution\n"
bash preprocessing.sh
printf "Preprocessing Finished Execution.\n"
printf "Finding Extremum Started Execution.\n"
bash finding_Extremum.sh
printf "Finding Extremum Finished Execution.\n"
printf "Growth Rate Started Execution.\n"
bash growth_Rate.sh
printf "Growth Rate Finished Execution.\n"
printf "Contribution of Subcategory Started Execution.\n"
printf "Please ignore the upcoming warnings. Outputs will be generated in .eps thus code throws warning.\n\n"
bash contribution_Of_Subcategory.sh
printf "Contribution of Subcategory Finished Execution.\n"
printf "Correlation and Inferential Analysis Started Execution.\n"
printf "Please ignore the upcoming warnings. Outputs will be generated in .eps thus code throws warning.\n\n"
bash correlation_And_Inferential_Analysis.sh
printf "Correlation and Inferential Analysis Finished Execution.\n"
printf "Project Execution Finished.\n"
printf "Thank you for your patience!\n"


