<template class="container" fluid style="height: 100vh;">
          <div class="home">
            

    <h1> 
    <pre>CADENA
            DE FAVORES </pre> 
    </h1>



    <section class="btn-container"> <!--
      <h2>Formulario Crear Nuevo Usuario o Loguearse</h2>
      
      -->
      <div class="list-container">
        <button  @click="onGoToPublicationsClicked">Ver las Publicaciones</button>
      </div>
      <br>
      <br>
      <div class="useractions">
        <button class="createuserbutton" @click="onCreateNewUserClicked">Registrarse</button>
          <article v-show="isCreateNewUserClicked">
            <UserFormComponent user_type="new" @sendingNewUser="onSavingNewUser" />   
          </article>
              
        <button class="loginbutton" @click="onLogInUserClicked">Iniciar Sesión</button>
          <article v-show="isLogInUserClicked">
            <h2>Seleccionar usuario precargado</h2>
            <select v-model="selectedUser">
              <option :value="null" disabled>Selecciona un usuario</option>
              <option v-for="user in usersList" :value="user" :key="user.id">
                {{user.user_id}} - {{ user.first_name }}  {{ user.last_name }}
              </option>
            </select>
            <button @click="choosingUser">Seleccionar Usuario</button>
          </article>
      </div>
    </section>


  <input type="checkbox" id="btn-modal">
	<label for="btn-modal" class="lbl-modal">Abrir Modal</label>
	<div class="modal">
    <div class="contenedor">
      <header>¡Bienvenidos!</header>
			<label for="btn-modal">X</label>
			<div class="contenido">
        <h3><!-- Agregar un titulo --></h3>
				<p><!-- Agregar un mensaje --></p>
			</div>
		</div>
	</div>
  
</div>
</template>

<script>
           
import { getUsers, saveNewUser} from "@/services/api.js";
import UserFormComponent  from "@/components/UserForm.vue"


export default {
  name: 'Home',
  components:{
    UserFormComponent,
    
},
  data() {
    return {
      publication_list: [],
      isCreateNewSeekForHelpClicked: false,
      isCreateNewOfferOfHelpClicked: false,
      isCreateNewUserClicked: false,
      isLogInUserClicked: false,
      selectedUser: null,
      usersList: []
    }
  },

  mounted() {
     
    
    this.loadData();
    /*
    if (localStorage.getItem('activeUserWatcher')) {
      try {
        this.selectedUser = JSON.parse(localStorage.getItem('activeUserWatcher'));
      } catch(e) {
        localStorage.removeItem('activeUserWatcher');
      }
    }
   **/

  },
  watch: {
    selectedUser:{

      handler(newSelectedUser){
             console.log("cambio detectado desde home")

        localStorage.activeUserWatcher = JSON.stringify(newSelectedUser);
      },
      deep: true
    }
  },
  
  methods: {
    async loadData() {
       this.usersList = await getUsers()
    },

    choosingUser() {

      /*
     let parsed = JSON.stringify(this.selectedUser);
      localStorage.setItem('activeUserWatcher', parsed);
      **/
      console.log("selectedUser HomePage: ", this.selectedUser)
      console.log("localUser HomePage activeUserWatcher: ", localStorage.activeUserWatcher)
     
      alert("usuario seleccionado!")
    // funciona


      // localStorage.removeItem('activeUserWatcher');

      window.localStorage.setItem('activeUserWatcher', JSON.stringify(this.selectedUser))
      console.log("selectedUser HomePage: ", this.selectedUser)
      
      window.location.reload(true);
     this.$router.push("/dashboard");

    },

    onGoToPublicationsClicked() { 
      // 1) Ir a la pagina de contactos
        this.$router.push("/publications");
    },


    onLogInUserClicked() { 
      console.log("clicked: onLogInUserClicked");
      this.isLogInUserClicked = !this.isLogInUserClicked

    },
    onCreateNewUserClicked() {
      console.log("clicked: onCreateNewUserClicked");
      this.isCreateNewUserClicked = !this.isCreateNewUserClicked
    },

    async onSavingNewUser(oneUser){
      console.log("usuario nuevo recibido del hijo: ", oneUser)
   
      console.log("guardando Usuario, first_name usuario:", oneUser.first_name)
      saveNewUser(oneUser)
      
      alert("Usuario creado!")
      window.location.reload(true);


    },
    onCreateNeedHelpPublicationClicked(){ //nuevo
            this.isCreateNewSeekForHelpClicked = !this.isCreateNewSeekForHelpClicked

    },
    onCreateOfferHelpPublicationClicked(){ //nuevo
            this.isCreateNewOfferOfHelpClicked = !this.isCreateNewOfferOfHelpClicked

    },




  }


}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
/*Còdigos universales de la pàgina*/
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Open Sans', sans-serif;;
}
/*Còdigo opcional - Fondo de la pàgina*/
body {
    background-size: 100vh 100vw;
    background-repeat: no-repeat;

}
/*---*/
body, .modal {
	width: 100%;
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
}

.modal {
	position: fixed;
	top: 0;
	left: 0;
	background: rgba(0,0,0,0.5);
	transition: all 500ms ease;
	opacity: 0;
	visibility: hidden;
}
#btn-modal:checked ~ .modal {
	opacity: 1;
	visibility: visible;
} 
.contenedor {
	width: 400px;
	height: 300px;
	margin: auto;
	background: #fff;
	box-shadow: 1px 7px 25px rgba(0,0,0,0.6);
	transition: all 500ms ease;
	position: relative;
	transform: translateY(-30%);
}
#btn-modal:checked ~ .modal .contenedor {
	transform: translateY(0%);
} 
.contenedor header {
	padding: 10px;
	background: #db8046;
	color: #fff;
}
.contenedor label {
	position: absolute;
	top: 10px;
	right: 10px;
	color: #fff;
	font-size: 15px;
	cursor: pointer;
}
.contenido {
	width: 100%;
	padding: 10px; 
}
.contenido h3 {
	margin-bottom: 10px;
}
.contenido p {
	margin-bottom: 7px;
}
#btn-modal {
	display: none;
}
.lbl-modal {
	background: #fff;
	padding: 10px 15px;
	border-radius: 4px;
	cursor: pointer;
}
@media only screen and (min-width:320px) and (max-width:768px) {
	.contenedor{
		width: 95%;
	}
}


.container {
  position: fixed;
  min-height: 100%;
  top:0;
  right: 0;
  bottom: 0;
  left: 0;
}

  h1 {
    font-family: 'Anton', sans-serif; 
    
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    font-size: 3em;
    color: whitesmoke;
  }

    
  .home {
    /**
      background-image: linear-gradient(to bottom left, blue,white);
    
    border-image-source: linear-gradient(60deg, #b16ec4,#5f97b9);
     border: solid;
    border-image-slice: 1;
    border-width: 5px;
    
    */
   display: flex;
   flex-direction: row ;
   font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    
   
  }
  .btn-container {
       display: flex;
       flex-direction: column;
       justify-content: space-between;
  }



  button {
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;

    border: 2px solid black;
    background-color: white;
    color: black;
    padding: 14px 28px;
    font-size: 16px;
    cursor: pointer;
    /**
    
    
    */
    border-color: #04AA6D;
    color: #04AA6D;
    text-shadow: 1px #837c7c;
    min-width: 13em;

  }

  button:hover {
    background-color: #04AA6D;

    color: white;
  }

  section {
    margin: 5em;
    display: flex;
    flex-direction: column;
    align-items: center;
          font: italic bold 1.5rem/150% Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;

  }




  article {
    
    justify-content: center;
    display: flex;
    flex-direction: column;
    padding: 2em;
    border-radius:1em;
    margin:0 auto;
    /** 
    
    background-color: #fbfbfb;
    border: 1px solid #04AA6D;
    */
    background-color:rgb(214, 218, 221);
    max-width: fit-content;
    }




  img:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }

</style>