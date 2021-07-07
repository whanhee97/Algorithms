function getIJ(input){
    ij=[];
    for(i = 0;i<8;i++){
        for(j = i+1; j<9;j++){
            if(total(i,j,input)==100){
                ij.push(i);
                ij.push(j);
                return ij;    
            }
        }
    }
}

function total(a1,a2,arr){
    sum = 0;
    for(x = 0; x<9; x ++){
        if(x != a1 && x != a2){
            sum += arr[x];
        }
    }
    return sum;
}

answer = [];
ij = getIJ(input);
i = ij[0];
j = ij[1];
for(a = 0; a<9; a++){
    if(a != i && a!= j){
        answer.push(input[a]);
    }
}
answer.sort(function(a,b){return a-b;});
console.log(answer);