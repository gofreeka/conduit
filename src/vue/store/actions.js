import Vue from "vue";
import axios from "axios";
import { router } from "../../public/js/_app.js";
import JwtService from "@/common/jwt_service.js";

const userDefault = {
   created_on: null,
   email: null,
   id: null,
   last_login: null,
   password: null,
   username: null,
};

export default {
  checkIfUserIsAuthenticated(context) {
    if (context.getters.user && context.getters.user.email) {
      console.log("Handling action: checkIfUserIsAuthenticated");
      axios
        .post("/users/login", {
          action: "check_auth",
          token: getCookie("drash_sess"),
          user_id: context.getters.user.id,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((response) => {
          console.log(response);
          context.dispatch("logOut");
        });
      return;
    }

    context.dispatch("logOut");
  },

  fetchArticles({ commit }, offset) {
    return new Promise((resolve) => {
      axios
        .get("/articles", {
          offset: offset
        })
        .then(({ data }) => {
          resolve(data)
        })
        .catch(error => {
          resolve(undefined);
        });
    });
  },

  fetchProfile({ commit }, params) {
    console.log(params);
    return new Promise((resolve) => {
      axios
        .get(`/profiles/${params.username}`)
        .then(({ data }) => {
          resolve(data)
        })
        .catch(error => {
          resolve(undefined);
        });
    });
  },

  fetchTags({ commit }) {
    return new Promise((resolve) => {
      axios
        .get("/tags")
        .then(({ data }) => {
          resolve(data)
        })
        .catch(error => {
          resolve(undefined);
        });
    });
  },

  logIn(context, credentials) {
    console.log("Handling action: logIn");
    return new Promise((resolve) => {
      axios
        .post("/users/login", {
          user: credentials
        })
        .then((response) => {
          console.log("Log in successful.");
          console.log(response);
          context.dispatch("setUser", response.data.user);
          resolve();
        })
        .catch((response) => {
          console.log("Log in unsuccessful.");
          console.log(response);
          context.dispatch("unsetUser");
          resolve();
        });
    });
  },

  logOut(context) {
    context.dispatch("unsetUser");
  },

  register(context, credentials) {
    return new Promise((resolve) => {
      axios
        .post("/users", {
          user: credentials
        })
        .then(({ data }) => {
          resolve(data);
        })
        .catch(() => {
          resolve(undefined);
        });
    });
  },

  setUser(context, user) {
    context.commit("setIsAuthenticated", true);
    context.commit("setUser", user);
    setCookie("drash_sess", user.token, 1);
  },

  unsetUser(context) {
    context.commit("setIsAuthenticated", false);
    context.commit("setUser", userDefault);
  }
};

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}