// cookies.js

import Cookies from 'js-cookie';

function saveValue(value) {
  Cookies.set('movie_title', value);
}

function saveType(type) {
  Cookies.set('movie_type', type);
}

function deleteCookie(value) {
  Cookies.remove(value);
}

function getValueFromCookie() {
  return Cookies.get('movie_title') || '';
}

function getTypeFromCookie() {
  return Cookies.get('movie_type') || '';
}

function saveInform(movieID) {
  Cookies.set('movie_ID', movieID);
  Cookies.set('informCheck', 'movieId');
}

function getIDFromCookie() {
  return Cookies.get('movie_ID') || '';
}

function saveFirstKey(key) {
  Cookies.set('firstKey', key);
}

function getFirstKey() {
  return Cookies.get('firstKey') || '';
}

export { 
  saveValue, saveType, 
  getValueFromCookie, getTypeFromCookie, 
  deleteCookie, 
  saveInform, getIDFromCookie, 
  saveFirstKey, getFirstKey, 
};
