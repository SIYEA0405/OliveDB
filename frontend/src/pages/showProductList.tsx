import { useQuery } from "@tanstack/react-query";
import { useRouter } from "next/router";
import { ProductDataProps } from "../../types";

import { fetchProducts } from "@/services/api";

import { Flex, Text } from "@chakra-ui/react";
import ProductTable from "@/components/ProductTable";

interface ShowProductListProps {
  products: ProductDataProps[];
}

const ShowProductList: React.FC<ShowProductListProps> = () => {
  const router = useRouter();
  const searchTerm = router.query.searchTerm;
  const { data, isLoading, error } = useQuery(
    ["products", searchTerm],
    () => fetchProducts(searchTerm),
    {
      staleTime: Infinity,
      enabled: !!searchTerm,
    }
  );
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    console.error(error);
  }

  return (
    <>
      <Flex alignItems="center">
        <Text as="b" mr={2} fontSize="lg" color="tomato">
          {searchTerm}
        </Text>
        <Text>
          검색결과 총 <Text as="b">{data?.length ?? 0}</Text>개
        </Text>
      </Flex>
      <ProductTable data={data} />
    </>
  );
};

export default ShowProductList;
