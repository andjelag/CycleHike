export class DateUtils{
    
    static months = ['Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Avg', 'Sep', 'Okt', 'Nov', 'Dec']

    static formatedDate(date:Date){
        let dateObject = new Date(date);
        return dateObject.getDate()+". "+this.months[dateObject.getMonth()]+" "+dateObject.getFullYear()
    }

    static dateInFuture(date:Date){
        const today = new Date();
        const dateObject = new Date(date);
        if(dateObject.getTime()>today.getTime())
            return true
        return false
    }

}