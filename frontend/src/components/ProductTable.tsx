import { useMemo } from "react";
import { Box, Table, Thead, Tbody, Tr, Th, Td } from "@chakra-ui/react";
import { useMediaQuery } from "@chakra-ui/react";
import {
  useReactTable,
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
} from "@tanstack/react-table";
import { ProductDataProps } from "../../types";
import { numberWithCommas } from "../../utils/numberUtils";

interface ProductTableProps {
  data: ProductDataProps[];
}

const columnHelper = createColumnHelper<ProductDataProps>();

export default function ProductTable({ data }: ProductTableProps) {
  const [isLargerThan768] = useMediaQuery("(min-width: 768px)");
  const columns = useMemo(() => {
    const columnDefs = [];

    if (isLargerThan768) {
      columnDefs.push(
        columnHelper.accessor("brand", {
          header: "브랜드",
          cell: (info) => info.getValue(),
        })
      );
    }

    columnDefs.push(
      columnHelper.accessor("name", {
        header: "상품명",
        cell: (info) => info.getValue(),
      })
    );

    if (isLargerThan768) {
      columnDefs.push(
        columnHelper.accessor("price.original", {
          header: "정가",
          cell: (info) => numberWithCommas(info.getValue()),
        })
      );
    }
    
    columnDefs.push(
      columnHelper.accessor("price.current", {
        header: "현재가",
        cell: (info) => numberWithCommas(info.getValue()),
      }),
      columnHelper.accessor("price.lowest", {
        header: "최저가",
        cell: (info) => numberWithCommas(info.getValue()),
      })
    );

    return columnDefs;
  }, [isLargerThan768]);

  const tableInstance = useReactTable({
    columns,
    data,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  return (
    <Box borderWidth="1px" borderRadius="md" overflowX="auto">
      <Table variant="simple" size={isLargerThan768 ? "md" : "sm"}>
        <Thead>
          {tableInstance.getHeaderGroups().map((headerGroup) => (
            <Tr key={headerGroup.id}>
              {headerGroup.headers.map((header) => (
                <Th key={header.id} textAlign="center" bg="#F4F4F4">
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                </Th>
              ))}
            </Tr>
          ))}
        </Thead>
        <Tbody>
          {tableInstance.getRowModel().rows.map((row, rowIndex) => (
            <Tr key={row.id} bg={rowIndex % 2 === 0 ? "gray.50" : "white"}>
              {row.getVisibleCells().map((cell) => (
                <Td key={cell.id} >
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </Td>
              ))}
            </Tr>
          ))}
        </Tbody>
      </Table>
    </Box>
  );
}
