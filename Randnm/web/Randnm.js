let set = `qwertyuiopasdfghjklzxcvbnm1234567890`
   function randlen() {
       return 8+Math.floor(Math.random()*4)
       }
   function randcode(len=randlen()) {
       var res = ""
       for(var i = 0; i < len; i++) {
           res += set[Math.floor(Math.random()*(set.length-1))]
           }
       return res
       };
   function randate(minage=20, curryear=2023) {
     var year = minage + Math.floor(Math.random()*minage),month = 1+ Math.floor(Math.random()*11), day
     if(month == 2) { day = 1 + Math.floor(Math.random()*27) }
     else if(month % 2 == 1) { day = 1+Math.floor(Math.random()*30) }
     else { day = 1+Math.floor(Math.random()*29) }
     return { day:  day, month: month, year: curryear-year}
     }
   function randnm() {
       var name = names[Math.floor(Math.random()*(names.length-1))]
       var surname = surnames[Math.floor(Math.random()*(surnames.length-1))]
       return { name: name, surname: surname }
      }
 
