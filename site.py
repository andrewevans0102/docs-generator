import os
import shutil

# global
md_files = []
project_folder = os.path.abspath(os.path.join(__file__ ,"../material2/"))
base_mkdocs = os.path.abspath(os.path.join(__file__ ,"../generated-site/base.yml"))
created_mkdocs = os.path.abspath(os.path.join(__file__ ,"../generated-site/mkdocs.yml"))
copied_folder = os.path.abspath(os.path.join(__file__ ,"../generated-site/docs/site-files/"))

# delete generated files and folders
def delete_files_and_folders():  
  shutil.rmtree(copied_folder, True)      
  shutil.rmtree(created_mkdocs, True)  
  print('deleted files and folders successfully')

# create initial files and folders
def create_files_and_folders():      
  os.makedirs(copied_folder)      
  os.makedirs(copied_folder + '/source')      
  os.makedirs(copied_folder + '/github')
  os.makedirs(copied_folder + '/guides')
  os.makedirs(copied_folder + '/project')
  shutil.copy(base_mkdocs, created_mkdocs)
  print('created files and folders successfully')  

# delete base yaml file to rebuild
def create_yaml():  
  shutil.copy(base_mkdocs, created_mkdocs)    
  print('created yaml file successfully') 

def select_md():  
  os.chdir(project_folder)  
  for root, dirs, files in os.walk(project_folder):      
    for file in files:        
      if file.endswith(".md"):          
        file_path = os.path.join(root, file)              
        print(file_path)            
        md_files.append(file_path)  

def copy_md():  
  # in order for the script to work correctly
  # as the files are copied the yaml file is updated
  # since this relationship cannot be seperated here
  # we have multiple loops for each group of files
  # performance improvements and innovation welcome
  with open(created_mkdocs, "a") as myfile:        
    myfile.write('  - source' + ':' + '\r')      
    counter = 0      
    for file_found in md_files: 
      if('/src/lib' in file_found):
        file_split = file_found.split('/')          
        copy_name = ''          
        display_name = ''     
        for split in file_split:   
          if '.md' in split:              
            copy_name = str(counter) + '-' + split                  
            display_name = str(counter) + '-' + split.replace('.md', '')           
            break        
        copied_file = copied_folder + "/source/" + copy_name             
        shutil.copy(file_found, copied_file)         
        myfile.write('    - ' + display_name + ': site-files/source/' + copy_name + '\r')          
        counter = counter + 1

  # github files
  with open(created_mkdocs, "a") as myfile:        
    myfile.write('  - github' + ':' + '\r')      
    counter = 0      
    for file_found in md_files: 
      if('.github' in file_found):
        file_split = file_found.split('/')          
        copy_name = ''          
        display_name = ''     
        for split in file_split:   
          if '.md' in split:              
            copy_name = str(counter) + '-' + split                  
            display_name = str(counter) + '-' + split.replace('.md', '')           
            break        
        copied_file = copied_folder + "/github/" + copy_name             
        shutil.copy(file_found, copied_file)         
        myfile.write('    - ' + display_name + ': site-files/github/' + copy_name + '\r')          
        counter = counter + 1

  # guides files
  with open(created_mkdocs, "a") as myfile:        
    myfile.write('  - guides' + ':' + '\r')      
    counter = 0      
    for file_found in md_files: 
      if('guides' in file_found):
        file_split = file_found.split('/')          
        copy_name = ''          
        display_name = ''     
        for split in file_split:   
          if '.md' in split:              
            copy_name = str(counter) + '-' + split                  
            display_name = str(counter) + '-' + split.replace('.md', '')           
            break        
        copied_file = copied_folder + "/guides/" + copy_name             
        shutil.copy(file_found, copied_file)         
        myfile.write('    - ' + display_name + ': site-files/guides/' + copy_name + '\r')          
        counter = counter + 1

  # project files
  with open(created_mkdocs, "a") as myfile:        
    myfile.write('  - project' + ':' + '\r')      
    counter = 0      
    for file_found in md_files: 
      if('guides' in file_found) or ('/src/lib' in file_found) or ('.github' in file_found):
        continue
      else:
        file_split = file_found.split('/')          
        copy_name = ''          
        display_name = ''     
        for split in file_split:   
          if '.md' in split:              
            copy_name = str(counter) + '-' + split                  
            display_name = str(counter) + '-' + split.replace('.md', '')           
            break        
        copied_file = copied_folder + "/project/" + copy_name             
        shutil.copy(file_found, copied_file)         
        myfile.write('    - ' + display_name + ': site-files/project/' + copy_name + '\r')          
        counter = counter + 1 

# Start
delete_files_and_folders()
create_files_and_folders()
select_md()
copy_md()