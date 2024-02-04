#include <stdio.h>

int numeros_perfeitos(int n1){

    int divisores = 0;


    for(int i = 1; i<n1; i++){
        if(n1%i == 0){

            divisores += i;
        }
    }

    if(divisores == n1){
        printf("Perfect");
    }

    else{ printf("No perfect");}

}

int main(){

    int n1;

    printf("Insira um numero: ");
    scanf("%d",&n1);

    numeros_perfeitos(n1);

    return 0;
}