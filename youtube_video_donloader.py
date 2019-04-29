import os
import shutil
import youtube_dl
import pafy
import sys
import urllib
from urllib.parse import urlparse


#Exceptions
class Error(Exception):
    pass

class PathNotFoundError(Error):
    pass

class InvalidURLerror(Error):
    pass


####################


#FUNCTIONS


def validate_url(in_url):

    """
    Objective:  To validate the input URL
    Input    :  Input URL
    Return   :  True- if valid
                False - if invalid
    """

    try:
        result = urlparse(in_url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def download(in_url, pref_type, save_path):
    """
        Objective:  To download video from the input URL
        Input    :  in_url - Input URL,
                    pref_type - Preferred video type,
                    save_path - Path to save the downloaded file
        Return   :  True- if Success
                    exits - if failure occurs
        """

    available_qualities = []
    try:
        video_obj = pafy.new(in_url)                #Create a new pafy object for the url
    except OSError as ose:
        print("Unable to visit the URL. There seems to be an internet connectivity issue.")
        sys.exit(1)

    streams = video_obj.streams                     #Creates a list of streaming qualities from pafy video object
    for qual in streams:
        available_qualities.append(str(qual).split(':')[1].split('@')[0].lower())

    print("The required video is available in the following qualities: ")
    for item in set(available_qualities):
        print(item, end=" ")

    #Get the preferred type from the user input value
    if pref_type == 'none':
        print("Preferred type is mentioned 'NONE'. So, downloading the best available quality")
        stream_obj = video_obj.getbest()

    #If the preferred type is available in the streaming qualities, download it. Or download the best available version
    if pref_type.lower() in available_qualities:
        print("\nThe preferred video type '{0}' is available. So downloading video in the preferred type.".format(pref_type))
        stream_obj = video_obj.getbest(preftype=pref_type)    #preftype=pref_type
    else:
        print("The video is not available in the desired quality i.e. {0}. Hence, downloading the best available quality".format(pref_type))
        stream_obj = video_obj.getbest()


    #Download the video using the stream object
    try:
        filename = stream_obj.download(quiet=False)
    except:
        print("Exception occurred while downloading.")
        sys.exit(1)

    #Checking if the video file exists already in the preferred path. If so, renaming the old file with '_old' extension
    video_path = os.path.join(save_path, filename)
    if os.path.isfile(video_path):
        print("The output file already exists in the specified path. So, renaming the old file with an extension '_old'")
        os.rename(video_path, str(video_path).split('.')[0] + "_old." + str(video_path).split('.')[1])


    #Moving the downloaded file to the desired path
    file_path = os.path.abspath(filename)
    base_file_name = os.path.basename(file_path)
    destination = os.path.join(save_path, base_file_name)
                         
    if shutil.move(os.path.join(os.getcwd(), base_file_name), destination):                     #We use shutil because, we can't move fron 'C:\' using os module.
        print("Successfully downloaded the video. It can be found at: \n {0}".format(destination))
        return True

    else:
        print("Unable to move the donwloaded file to the desired location. It can be found at \n {0}".format(file_path))
        return True


##############

"""This is the main function"""
def main():

    """
    Objective   : Gets the user inputs and validates them. Calls the necessary functions for operating on those inputs
    Return      : 0 - if Success
                 -1 - if download fails
                  1 - if exception occurs
    """
    try:
        in_url = input("Enter the desired url: ")
        ret = validate_url(in_url)                  #Validates the URL right awaay and throws exception if validation failed
        if not ret:
            raise InvalidURLerror

        pref_type = input("Enter the prefered video type (eg. mp4) | Enter 'none' if there's not preference: ")
        save_path = input("Enter the desired path to save the video file: ")

        if os.path.isdir(save_path):                #Validates the preferred path
            pass
        else:
            raise PathNotFoundError

        if download(in_url, pref_type, save_path):
            sys.exit(0)
        else:
            sys.exit(-1)


    except PathNotFoundError as pnferr:
        print("Given Path to save the video is not valid. Please try again later with a valid path.")
        sys.exit(1)

    except InvalidURLerror as inurlerr:
        print("Please provide a valid video URL. There seems to be a problem with the URL")
        sys.exit(1)

if __name__ == "__main__":
    main()
