<template>
  <section class="user-data">
    
    <label for="firstName">Nombre:</label>
    <input type="text" key="firstName" v-model="userInForm.first_name"/>

    <label for="lastName">Apellidos:</label>
    <input
      type="text"
      id="lastName"
      v-model="userInForm.last_name"
    />
    <label for="email">E-mail:</label>
    <input
      type="email"
      id="email"
      v-model.trim="userInForm.email"
    />
   <!--
<label for="phone">Teléfono:</label>
    <input
      type="tel"
      id="phone"
      v-model="userInForm.phone"
    />

   --> 
    
    <button @click="onCreateNewUser">
      Crear usuario
    </button>
  </section>
  <br />
  
 <!-- Hijo: {{ $data }}-->


</template>

<script>
import { v4 as uuidv4 } from "uuid";

export default {
    name: "UserFormComponent",
    props: {
        user_type: { //borrar prop
            type: String,
            required: true
        }
    },
    emits: ["sendingNewUser"],


    data() {
        return {

            userInForm: {},
            received_user: this.user_type 
            // userInForm: this.user       
        }
    }, 
    methods: {
        onCreateNewUser(){

          this.userInForm.user_id = uuidv4();
          this.$emit("sendingNewUser", this.userInForm)         
        }
    }

}
</script>

<style scoped>


.user-data {
  box-sizing: border-box;
  margin: 2em 2em 2em 2em;
  padding: 1em;
  border-radius: 0.5em;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.user-data label {
  display:inline-block;
  font-weight: bold;
}

.user-data input {
  box-sizing: border-box;
  background: none;
  border:none;
  outline: none; /** para cuando se escribe que no salga un cuadrado negro */
  border-bottom: 2px solid white;
  margin-bottom: 1.5em;
}


.user-data input:focus {
  border-bottom: 3px solid white;
  background-color: white; 
  /**
  nota1: creo que queda mejor sin background, revisar
  nota2: con el background no se nota el cambio del border bottom de 2 a 3px */

}

button {
  align-self: center;
}
</style>