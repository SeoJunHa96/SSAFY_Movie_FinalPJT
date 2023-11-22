import axios from 'axios';

const config = {
    baseURL : 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&detail=Y&listCount=100&sort=prodYear,1&',
    myKey : '9344J1T8LM90EMLN4H82',
}

function movieSearch(searchtxt) {
    const baseURL = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&detail=Y&listCount=100&sort=prodYear,1&'
    const myKey = '9344J1T8LM90EMLN4H82'
    return axios.get(`${baseURL}${searchtxt}&ServiceKey=${myKey}`);
}


export { movieSearch } 