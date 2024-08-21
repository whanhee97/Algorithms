import java.util.*;

class Music implements Comparable<Music>{
    String g;
    int no;
    int play;
    public Music(String g, int no, int play){
        this.g = g;
        this.no = no;
        this.play = play;
    }
    @Override
    public int compareTo(Music t){
        return  t.play != this.play ? t.play-this.play : this.no - t.no; // 플레이 기준 내림차순, 고유번호 오름차순
    }
}

class prog42579 {
    public int[] solution(String[] genres, int[] plays) {

        Map<String,Integer> total = new HashMap<>(); // 장르별 총 플레이수 저장
        Map<String,ArrayList<Music>> hm = new HashMap<>(); // 장르별 Music 저장
        for(int i=0;i<genres.length;i++){
            String genre = genres[i];
            int play = plays[i];
            total.put(genre, total.getOrDefault(genre,0)+play); // 장르별 플레이수 집어넣고

            Music tmp = new Music(genre,i,play);
            ArrayList<Music> tmpArr = hm.getOrDefault(genre, new ArrayList<>());
            tmpArr.add(tmp);
            hm.put(genre,tmpArr); // 장르에 해당하는 Music 넣기
        }
        ArrayList<Integer> ans = new ArrayList<>();

        List<Map.Entry<String,Integer>> entryList = new ArrayList<>(total.entrySet()); // 엔트리 리스트 만들고
        Collections.sort(entryList, (a,b)-> total.get(b.getKey()) - total.get(a.getKey())); // total 정렬(value 기준) -> 제일 플레이 많은 장르별로 정렬 될것임.

        for(Map.Entry<String,Integer> entry : entryList){
            String genre = entry.getKey(); // 제일 플레이 많은 장르 순서대로 가져와서
            ArrayList<Music> mArr = hm.get(genre); //그 장르에 해당하는 Music 리스트를 꺼내고
            Collections.sort(mArr); // 뮤직리스트 정렬
            if(mArr.size() == 1){
                ans.add(mArr.get(0).no);
            }else{
                ans.add(mArr.get(0).no);
                ans.add(mArr.get(1).no);
            }
        }
        int size = ans.size();
        int[] answer = new int[size];
        for(int i=0;i<size;i++){
            answer[i] = ans.get(i);
        }
        return answer;
    }
}