import { TableContainer, Table, Tbody, Tr, Td } from "@chakra-ui/react";
import { ProductDataProps } from "../../types";

export default function ProductTable({ ...productData }: ProductDataProps) {
  return (
    <>
      <TableContainer>
        <Table variant="simple">
          <Tbody>
            <Tr>
              <Td>상품번호(ID)</Td>
              <Td>{productData._id}</Td>
            </Tr>
            <Tr>
              <Td>이름(Name)</Td>
              <Td>{productData.name}</Td>
            </Tr>
            <Tr>
              <Td>브랜드(Brand)</Td>
              <Td>{productData.brand}</Td>
            </Tr>
            <Tr>
              <Td>가격(정가)</Td>
              <Td>{productData.price.original}</Td>
            </Tr>
            <Tr>
              <Td>가격(현재가)</Td>
              <Td>{productData.price.current}</Td>
            </Tr>
            <Tr>
              <Td>가격(역대최저가)</Td>
              <Td>{productData.price.lowest}</Td>
            </Tr>
            <Tr>
              <Td>메인 카테고리</Td>
              <Td>{productData.large_ctg}</Td>
            </Tr>
            <Tr>
              <Td>세부 카테고리</Td>
              <Td>{productData.small_ctg}</Td>
            </Tr>
          </Tbody>
        </Table>
      </TableContainer>
    </>
  );
}
