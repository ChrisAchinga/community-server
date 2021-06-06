const slugify = require("slugify");

module.exports = {
  lifecycles: {
    beforeCreate: async (data) => {
      if (data.fullName) {
        data.slug = slugify(data.fullName, { lower: true });
      }
    },
    beforeUpdate: async (params, data) => {
      if (data.fullName) {
        data.slug = slugify(data.fullName, { lower: true });
      }
    },
  },
};
