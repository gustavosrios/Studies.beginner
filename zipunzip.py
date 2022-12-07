import zipfile
import shutil
f = open('fileone.txt', 'w')
f.write('Text in File one')
f.close()
f = open('filetwo.txt', 'w')
f.write('Text in File two')
f.close()

#create zip files
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_object = zipfile.ZipFile('comp_file.zip','r')
zip_object.extractall('files_here') # nome da pasta que os itens extraidos irao


dir_to_zip = 'C:\\Users\\gusta\\OneDrive\\Área de Trabalho\\python_bootcamp\\files_here'
output_filename = 'files_here_zip'
shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('files_here_zip.zip','final_unzip','zip')