#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#define NUM_THREADS     5       

static int fn()
{
//        printf("Visisted dir\n");
        return 0;
}




void *PrintHello(void *threadid)
{
   long tid;
   tid = (long)threadid;
//   printf("Hello World! It's me, thread #%ld!\n", tid);
   FILE *f;
   f=fopen("myfile.txt","r");
   fseek(f, 0, SEEK_END);
   long fsize = ftell(f);
   fseek(f, 0, SEEK_SET);

   char *string = malloc(fsize + 1);
   fread(string, fsize, 1, f);
//   printf("%s\n\n\n",string);
   fclose(f);

   pthread_exit(NULL);
}

int main(int argc, char *argv[])
{

   int no=strtol(argv[1],NULL,0);
   pthread_t threads[no];
   int rc;
   long t;
   for(t=0;t<no;t++){
//     printf("In main: creating thread %ld\n", t);
     rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
     if (rc){
       printf("ERROR; return code from pthread_create() is %d\n", rc);
       exit(-1);
       }
     }

   /* Last thing that main() should do */
   pthread_exit(NULL);
}
