function solution(a, b) {
    var answer = '';
    var month = [0,31,29,31,30,31,30,31,31,30,31,30,31];
    var arr = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    var days = 0;
    for( var i = 0; i < a; i++){
        days += month[i];
    }
    days += b;
    answer = arr[days%7]
    
    return answer;
}

console.log(solution(3,17));