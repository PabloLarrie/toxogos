-
<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">
        <b-button>
          <router-link to="/">Home</router-link>
        </b-button>
        ToXogos
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-button>
            <router-link to="/Games">Games</router-link>
          </b-button>
          <b-button>
            <router-link to="/decks">Designers</router-link>
          </b-button>
          <b-button>
            <router-link to="/login">Login</router-link>
          </b-button>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
  data() {
    return {};
  },
};
</script>
<style scoped>
</style>