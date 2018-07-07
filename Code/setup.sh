echo 'created by Pranav'

pip install wget
apt-get install aria2
pip install kaggle
pip3 install urllib3
pip install pydot

#To setup Google Drive
apt-get install -y -qq software-properties-common python-software-properties module-init-tools
add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
apt-get update -qq 2>&1 > /dev/null
apt-get -y install -qq google-drive-ocamlfuse fuse

echo ">>>>>>>>>>>> Getting Kaggle authentication token <<<<<<<<<<<

#If you have not already saved Kaggle token on google drive, sign up for a Kaggle account at https://www.kaggle.com. 
#Then go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'. 
#This will trigger the download of kaggle.json, a file containing your API credentials.  

#Go to your Google Drive and place the kaggle.json file where your Google Colab notebooks are saved. Then execute the following."




#wget https://raw.githubusercontent.com/thegreatskywalker/my_deep_learning/master/Scripts/google_drive_authentication.py 	
#chmod +x google_drive_authentication.py
#python google_drive_authentication.py


