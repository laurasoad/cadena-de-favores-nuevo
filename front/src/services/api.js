import config from "@/config.js";

export function getUserId() {
  // Si no está la condición, da error al intentar cargarlo

    //  activeUser = JSON.parse(localStorage.getItem("activeUserWatcher"));
    const activeUserJson = localStorage.getItem("activeUserWatcher")
    const user = JSON.parse(activeUserJson);
    return user.user_id;
  
}


export async function getUsers() { //No Auth (por ahora)
    
  const response = await fetch(`${config.API_PATH}/users`);
  const user_list = await response.json();
  return user_list;
}

export async function saveNewUser(newUser) { //No Auth (por ahora)
    
  const settings = {
    method: "POST",
    body: JSON.stringify(newUser),
    headers: {
        "Content-Type": "application/json",
    },
}
await fetch(`${config.API_PATH}/users`, settings);
}



// Obtener mis publicaciones 
// TAREA: add user_id to /api/contacts

// def test_should_return_list_of_contacts_by_user():
// BACK aún no está en el webserver
// BACK ni el metodo en el repo de publications
/**
 * 
     @app.route("/api/contacts", methods=["GET"])
   
    def contacts_get_all_by_user():
        user_id = request.headers.get('Authorization')
        all_contacts = repositories["publications"].get_publications_of_this_user(user_id)
        return object_to_json(all_contacts)

 */


export async function getPublications() { // No Auth
    
    const response = await fetch(`${config.API_PATH}/publications`);
    const pub_list = await response.json();
    return pub_list;
}
  


export async function addPublication(newPub) { //Auth
    const settings = {
        method: "POST",
        body: JSON.stringify(newPub),
        headers: {
            "Content-Type": "application/json",
             Authorization: getUserId(),
        },
    }
    await fetch(`${config.API_PATH}/publications`, settings);

}
  
export async function getPublicationById(pubId){ //No Auth
 
    const settings = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
   
    const response = await fetch(
      `${config. API_PATH}/publications/${pubId}`,
      settings);

    let publication = await response.json();

    return publication
}




export async function editPublication(publication) { //Auth
    const settings = {
      method: "PUT",
      body: JSON.stringify(publication),
      headers: {
        "Content-Type": "application/json",
        Authorization: getUserId(),
      },
    };
    await fetch(`${config.API_PATH}/publications/${publication.id_pub}`, settings);
}


export async function deletePublicationById(id_publication) { //Auth
  //    body: JSON.stringify(id_publication),
  
  const settings = {
    method: "DELETE",
    body: "",
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),    },
  };
  await fetch(`${config.API_PATH}/publications/${id_publication}`, settings);
}


