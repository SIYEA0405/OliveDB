import axios from "axios";
export const fetchProducts = async (searchTerm: string) => {
  const response = await axios.get("/api/getProducts", {
    params: {
      search: searchTerm,
    },
  });
  return response;
};

