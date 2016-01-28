#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#define NUM_THREADS     500

static int fn()
{
//        printf("Visisted dir\n");
        return 0;
}




void *PrintHello(void *threadid)
{
   long tid;
   tid = (long)threadid;
   //printf("Hello World! It's me, thread #%ld!\n", tid);
   if (ftw(".", fn, 10) != 0) {
                printf("Error\n");
                pthread_exit(NULL);
        }

   pthread_exit(NULL);
}

int main(int argc, char *argv[])
{


   int no=strtol(argv[1],NULL,0);
  struct timespec start, end;
   pthread_t threads[no];
   int rc;
   long t;
   //int no=strtol(argv[1],NULL,0);
  // clock_gettime(CLOCK_MONOTONIC, &start);
   for(t=0;t<no;t++){

	//printf("In main: creating thread %ld\n", t);
     rc = pthread_create(&threads[t], NULL, PrintHello, (void *)t);
     if (rc){
       printf("ERROR; return code from pthread_create() is %d\n", rc);
       exit(-1);
       }
     }

   /* Last thing that main() should do */
  // pthread_exit(NULL);
//   clock_gettime(CLOCK_MONOTONIC, &end);
//long  accum = ( end.tv_sec - start.tv_sec )+ ( end.tv_nsec - start.tv_nsec );
//printf("Time elapsed= %ld",accum);

   pthread_exit(NULL);
}

