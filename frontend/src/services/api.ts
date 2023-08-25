import axios from "axios";
type SearchTermProps = string | string[] | undefined;

export const fetchProducts = async (searchTerm: SearchTermProps) => {
  const response = await axios.get("/api/getProducts", {
    params: {
      search: searchTerm,
    },
  });
  return response.data;
};
