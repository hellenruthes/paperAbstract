from re import I
import src.list_papers as listpaper
import src.pdf_to_txt as pdftotxt
import src.save_txt_file as savefile
import src.directories as d
import logging


#variables
dir = '/Users/hellenruthes/Downloads/bulk-download (1)/' #define your source pdf file

#------------------

files_array = listpaper.list_files(dir)

if __name__ == "__main__":
    #d.remove_output_file(dir+"output/output.txt")
    d.create_dir(dir, "output") #creates output dir
    i=1
    for file in files_array:
        if(file[-3:]=='pdf'): #to guarantee only pdf files 
            try:
                s = pdftotxt.pdf_file_obj(dir,file)
                first = 'Abstract'
                last = 'Keywords'
                abstract = pdftotxt.get_piece_of_text(s, first,last)
                identificator = "**** article"+str(i)+" "+file[:-4]
                i = i + 1
                savefile.save_txt_file(dir,identificator)
                savefile.save_txt_file(dir,abstract)
                logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')
                logging.warning("NO errors - %s", file[:-4])
            except:
                logging.error("ERRORS - %s ", file[:-4])
             
            