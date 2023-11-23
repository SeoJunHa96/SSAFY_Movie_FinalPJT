    <script setup>
    import { ref } from 'vue'
    import { useCounterStore } from '@/stores/counter'
    
    const store = useCounterStore()
    const username = ref(null)
    const nickname = ref(null)
    const password1 = ref(null)
    const password2 = ref(null)
    
    const signUp = function () {
      const payload = {
        username: username.value,
        nickname: nickname.value,
        password: password1.value,
        password2: password2.value
      }
      store.signUp(payload)
    }
    
    
    </script>
    
    <template>
      <div class="formbox">
        <div class="signup-form">
          <h1>회원가입</h1>
          <form @submit.prevent="signUp" >
            <div class="form-group">
              <label for="username">아이디 </label>
              <input class="placeholdercolor" placeholder="아이디를 입력하세요" type="text" id="username" v-model.trim="username">
            </div>
            
            <div class="form-group">
              <label for="nickname">활동명: </label>
              <input class="placeholdercolor" placeholder="활동명을 입력하세요" type="text" id="nickname" v-model.trim="nickname">
            </div>
            
            <div class="form-group">
              <label for="password1">비밀번호: </label>
              <input class="placeholdercolor" placeholder="비밀번호를 입력하세요" type="password" id="password1" v-model.trim="password1">
            </div>
            
            <div class="form-group">
              <label for="password2">비밀번호 확인: </label>
              <input class="placeholdercolor" placeholder="비밀번호를 한번 더 입력하세요" type="password" id="password2" v-model.trim="password2">
            </div>
            
            <button type="submit">가입하기</button>
          </form>
        </div>
      </div>
    </template>
    
    
<style scoped>
/* Signup form styles */
.signup-form {
  width: 500px;
  margin: 0 auto;
  font-family: 'Poppins', sans-serif;
  color: #fff;
  width: 100%;
}
.formbox {
    font-family: poppins;
    background-color: rgba(0, 0, 0, 0.5);
    margin: auto auto;
    padding: 40px;
    border-radius: 5px;
    box-shadow: 0 0 10px #000;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 600px;
    height: 630px;
    justify-content: center; /* 수평 가운데 정렬 */
    align-items: center;

}

h1 {
  font-size: 32px;
  font-weight: 600;
  padding-bottom: 30px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-size: 18px;
  font-weight: 500;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  border-radius: 5px;
  border: none;
  border-bottom: 2px solid #fff;
  background-color: transparent;
  color: #fff;
  font-size: 16px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-bottom: 2px solid #3498db;
}

button {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #3498db;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 18px;
}

button:hover {
  background-color: #2980b9;
}
.placeholdercolor::placeholder{
  color: white
}
</style>