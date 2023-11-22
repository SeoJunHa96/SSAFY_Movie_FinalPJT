import { createStore } from 'vuex';
import { getValueFromCookie, getTypeFromCookie, getIDFromCookie, getFirstKey } from '../utils/cookies';
import axios from 'axios';

function movieSearch(searchtxt) {
  const baseURL = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&detail=Y&listCount=100&sort=prodYear,1&'
  const myKey = '9344J1T8LM90EMLN4H82'
  return axios.get(`${baseURL}${searchtxt}&ServiceKey=${myKey}`);
}


const state = {
  moviedata: [],
  result: [],
  searchTxtBox: {
    searchTxt: getValueFromCookie() || '',
    check: getTypeFromCookie() || '',
  },
  keywordFirstBox: {
    searchTxt: getFirstKey() || '',
    check: '',
  },
  similarMoviedata: [],
  movieID: {
    searchTxt: getIDFromCookie() || '',
  },
  likeMovies: [],
};

const mutations = {
  SET_URL(state, data) {
    state.moviedata = data;
    state.result = data.Data[0].Result;
  },
  STATE_UTL(state, searchTxtBox) {
    state.searchTxtBox = searchTxtBox;
  },
  MOVIE_ID(state, id) {
    state.movieID = id;
  },
  SIMILAR_MOVIE_API(state, keywordFirstBox) {
    state.keywordFirstBox = keywordFirstBox;
  },
  SIMILAR_MOVIES(state, data) {
    state.similarMoviedata = data;
  },
};

const actions = {
  async FETCH_TITLE(context, data) {
    try {
      const res = await movieSearch(data.searchTxt);
      context.commit('SET_URL', res.data);
      return res;
    } catch (err) {
      console.log(err);
    }
  },
  async KEY_SIMILAR(context, data) {
    try {
      const res = await movieSearch(data.searchTxt);
      context.commit('SIMILAR_MOVIES', res.data);
      return res;
    } catch (err) {
      console.log(err);
    }
  },
};

export default createStore({
  state,
  mutations,
  actions,
  modules: {},
});
