import { TableContainer, Table, Tbody, Tr, Td } from "@chakra-ui/react";
export default function ProductTable() {
  return (
    <>
      <TableContainer>
        <Table variant="simple">
          <Tbody>
            <Tr>
              <Td>상품번호(ID)</Td>
              <Td>A1234</Td>
            </Tr>
            <Tr>
              <Td>이름(Name)</Td>
              <Td>수분크림</Td>
            </Tr>
            <Tr>
              <Td>브랜드(Brand)</Td>
              <Td>millimetres (mm)</Td>
            </Tr>
            <Tr>
              <Td>가격(정가)</Td>
              <Td>10000</Td>
            </Tr>
            <Tr>
              <Td>가격(현재가)</Td>
              <Td>8000</Td>
            </Tr>
            <Tr>
              <Td>가격(역대최저가)</Td>
              <Td>5000</Td>
            </Tr>
            <Tr>
              <Td>메인 카테고리</Td>
              <Td>스킨</Td>
            </Tr>
            <Tr>
              <Td>세부 카테고리</Td>
              <Td>스킨/로션/기타</Td>
            </Tr>
          </Tbody>
        </Table>
      </TableContainer>
    </>
  );
}
