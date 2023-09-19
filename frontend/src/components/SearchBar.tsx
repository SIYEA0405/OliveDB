import React, { useState } from "react";
import { useRouter } from "next/router";
import { useQueryClient } from "@tanstack/react-query";
import {
  InputGroup,
  InputLeftElement,
  InputRightElement,
  Input,
  Button,
} from "@chakra-ui/react";
import { AiOutlineSearch, AiOutlineSend } from "react-icons/ai";

import { fetchProducts } from "@/services/api";

interface SearchBarProps {}

const SearchBar: React.FC<SearchBarProps> = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const router = useRouter();
  const queryClient = useQueryClient();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const data = await fetchProducts(searchTerm);
      queryClient.setQueryData(["products", searchTerm], data);
      if (data.length === 1) {
        router.push({
          pathname: "/showProduct",
          query: { id: data[0]._id },
        });
      } else {
        router.push({
          pathname: "/showProductList",
          query: { searchTerm: searchTerm },
        });
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      event.preventDefault();
      handleSubmit(event);
    }
  };
  return (
    <>
      <InputGroup border="3px solid #BBD94E" borderRadius="full">
        <InputLeftElement pointerEvents="none">
          <AiOutlineSearch className="icon" />
        </InputLeftElement>
        <Input
          border="none"
          placeholder="제품 이름을 입력해주세요"
          _focus={{
            outline: "none",
            boxShadow: "none",
          }}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />
        <InputRightElement width="4rem">
          <Button h="1.75rem" size="sm" onClick={handleSubmit} bg="#C3D973">
            <AiOutlineSend color="#666666" />
          </Button>
        </InputRightElement>
      </InputGroup>
    </>
  );
};

export default SearchBar;
