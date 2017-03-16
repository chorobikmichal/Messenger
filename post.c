#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "stream.h"
#include <time.h>

/*
*Michal Chorobik 0937145*mchorobi@uofguelph.mail.ca*February 19, 2017*/

struct PostEntry {
  void (*formatEntry)(struct PostEntry* this ,struct userPost *st ,char * arg[99],char * stream[99],char * text[99]);
  void (*readInput)(struct PostEntry* this ,char * stream[99],char * text[99]);
  void (*getTimeDate)(struct PostEntry* this ,struct userPost *st );
  void (*submitPost)(struct PostEntry* this ,struct userPost *st );
};


void formatEntry(struct PostEntry* this , struct userPost*st,char*arg[99],char*stream[99],char*text[99]){
    /*creates the struct used by the updateStream() function*/


    (*st).username=*arg;
    (*st).streamname=*stream;
    (*st).text[0]=*text;

    /*printf("%s\n",(*st).username );*/

    /*printf("%s\n",(*st).streamname );*/

    /*printf("%s\n",(*st).text[0] );*/


  }
void readInput(struct PostEntry* this , char* stream[99],char* text[99]){
    /*reads the user's input to the post program*/


      char tempText[99];

      printf("stream: ");
      fgets(*stream,99,stdin);
      /**stream[strlen(*stream)-1]='\0';*/


      printf("enter text: ");
      fgets(tempText,99,stdin);
      tempText[strlen(tempText)-1]='\0';

      if(strcmp(tempText,"ctrl-d")!=0){
        strcpy(*text,tempText);
        printf("- ");
        fgets(tempText,99,stdin);
        tempText[strlen(tempText)-1]='\0';
      }

      while (strcmp(tempText,"ctrl-d")!=0) {
        strcat(*text,"\r\n");
        strcat(*text,tempText);
        printf("- ");
        fgets(tempText,99,stdin);
        tempText[strlen(tempText)-1]='\0';
      }

  }
void getTimeDate(struct PostEntry* this , struct userPost*st){/*determines the current time and date and formats it as a string*/


    /*the stuff below gives the time and date example: Tue Feb 14 14:46:56 2017*/

    time_t rawtime;
    struct tm * timeinfo;
    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    /*printf ( "Current local time and date: %s", asctime(timeinfo));*/

    (*st).date=asctime(timeinfo);

  }
void submitPost(struct PostEntry* this , struct userPost*st){/*calls the updateStream() function*/

    updateStream(st);
  }


void constructorPostEntry (struct PostEntry* this) {
	this->formatEntry = &formatEntry;
	this->readInput = &readInput;
	this->getTimeDate = &getTimeDate;
	this->submitPost = &submitPost;
	}



int main(int argc, char const *argv[]) {
  struct PostEntry PostEntry;
constructorPostEntry(&PostEntry);
  char author[99];
  strcpy(author,argv[1]);
  char *ptr1=author;
  char stream[99];
  char *ptr2=stream;
  char text[99];
  char *ptr3=text;

  struct userPost userPost;
  struct userPost* spt = &userPost;

  PostEntry.readInput(&PostEntry, &ptr2,&ptr3);
  ptr2[strlen(ptr2)-1]='\0';
  PostEntry.formatEntry(&PostEntry, spt,&ptr1,&ptr2,&ptr3);

  /*by here the stream name, author and the text are added into the struct*/

  /*update stream posts the post to the stream*/

  PostEntry.getTimeDate(&PostEntry, &userPost);
  PostEntry.submitPost(&PostEntry, &userPost);

  /*printf("username: %s\n",(*spt).username );*/

  /*printf("streamname: %s\n",(*spt).streamname );*/

  /*printf("text: %s\n",(*spt).text[0] );*/

  /*printf("date: %s\n",(*spt).date );*/


  return 0;
}
