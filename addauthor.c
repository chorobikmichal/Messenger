#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "stream.h"

/*
*Michal Chorobik 0937145
*mchorobi@uofguelph.mail.ca
*February 19, 2017
*/

int main(int argc, char const *argv[]) {
  int remove=0;
  char author[99];

  if(argc == 2){
    strcpy(author,argv[1]);
  }else if(argc > 2){
    strcpy(author,argv[2]);
    remove=1;
  }else{
    exit(0);
  }

  char streamList[99];

  printf("list streams: ");
  fgets(streamList,99,stdin);
  streamList[strlen(streamList)-1]='\0';

  char *ptr1=author;
  char *ptr2=streamList;

  if(remove==1){
    removeUser(ptr1,ptr2);
  }else{
    addUser(ptr1,ptr2);
  }

  return 1;
}
