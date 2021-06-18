<template>
  <b-container>
    <b-row>
      <slot name="gameBody" />
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "GameLayout",
};
</script>