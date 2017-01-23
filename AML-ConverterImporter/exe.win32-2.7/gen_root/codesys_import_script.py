'''
Created on 18.06.2015

@author: george
'''
from __future__ import print_function
import sys, os, scriptengine , System.Diagnostics
import csv

GEN_ROOT = r"C:\Users\george\Desktop\SVN\OPAKStudents\Amil George\exe\exe.win32-2.7\gen_root\importable";
PROJECT = r"C:\Windows\Temp\test.project"


FB = "FB"
MD = "MD"
INTERFACE = "Interface"

class Reporter(ImportReporter):
   def error(self, message):
      system.write_message(Severity.Error, message)

   def warning(self, message):
      system.write_message(Severity.Warning, message)

   def resolve_conflict(self, obj):
      return ConflictResolve.Copy

   def added(self, obj):
      print("added: ", obj)

   def replaced(self, obj):
      print("replaced: ", obj)

   def skipped(self, obj):
      print("skipped: ", obj)

   @property
   def aborting(self):
      return False




def check_and_create_folder(parent, folder_name):
    objs = parent.find(folder_name)
   
    if  objs and objs[0].is_folder:
        return objs[0]
    else:
        parent.create_folder(folder_name)
        new_objs= parent.find(folder_name)
        new_folder =  new_objs[0]
        
        return new_folder
        
def walk_to_path(proj,dst_path):
    path_arr=dst_path.split("/")
    #print(path_arr)
    parent = proj
    for folder_name in path_arr:
        #print(folder_name)
        parent=check_and_create_folder(parent, folder_name)
        
    return parent

def create_pou(proj,type,name,dst_path,src_path):
    imp_reporter = Reporter()
    loc=walk_to_path(proj, dst_path)
    file_path = os.path.join(GEN_ROOT,src_path)
    
    if type == MD:
    	with open(file_path, 'r') as f:
            read_data = f.read()
            mdObj=modulerepository.create_module_declaration_object(name, read_data)
            mdObj.move(loc)
    elif type == FB:
        #print(loc)
        #print(loc.is_folder)
        path_arr=dst_path.split("/")
        
        #new_locs=proj.find("Component",True)
        #print(new_locs)
        #print("NEW")
        #new = new_locs[0]
       
        proj.import_xml(imp_reporter,file_path,True)
    elif type == INTERFACE:
        #pass
        proj.import_xml(imp_reporter,file_path,True)
         
        
    
    
    
def execute(gen_root_loc = GEN_ROOT ):
    
    
    
    if projects.primary:
       projects.primary.close()
    
    gen_root = os.path.abspath(gen_root_loc)
    proj = projects.create(PROJECT)
    prim = projects.primary
    imp_reporter = Reporter()
    gen_list_filepath= os.path.join(gen_root,'gen_list.csv')
    with open(gen_list_filepath, "rb") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
            type = row[0]
            name = row[1]
            dst_path = row[2]
            src_path = row[3]
            file_path = os.path.join(gen_root,src_path)
            #proj.import_xml(imp_reporter,file_path)
            
            create_pou(prim,type, name, dst_path, src_path)
            


execute()
#print(sys.argv)